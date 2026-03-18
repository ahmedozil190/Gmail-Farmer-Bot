from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import get_user, get_business_config
from strings import STRINGS

def get_required_channels():
    conf = get_business_config()
    raw = conf.get("REQUIRED_CHANNELS", "")
    if not raw:
        return []
    
    channels = []
    for c in raw.split(","):
        c = c.strip()
        if not c:
            continue
        
        # If it's a URL like https://t.me/channelname, extract @channelname
        if "t.me/" in c:
            username = c.split("t.me/")[-1].strip("/")
            channels.append(f"@{username}")
        else:
            # Ensure it's a clean username with @
            username = c.replace("@", "")
            channels.append(f"@{username}")
            
    return list(set(channels)) # Unique list

async def check_subscriptions(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    channels = get_required_channels()
    unsubscribed = []
    
    # Debug logging
    with open("crash.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Checking subs for {user_id}. Target channels: {channels}\n")
    
    for channel in channels:
        try:
            # Ensure it starts with @ if it's a username
            chat_id = channel if channel.startswith("@") else f"@{channel}"
            member = await context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            
            with open("crash.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] User {user_id} in {channel} status: {member.status}\n")
                
            if member.status not in ['member', 'administrator', 'creator']:
                unsubscribed.append(channel)
        except Exception as e:
            with open("crash.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] Error checking {channel}: {str(e)}\n")
            print(f"Error checking subscription for {channel}: {e}")
            unsubscribed.append(channel) # If bot can't check, assume not subscribed
            
    return unsubscribed

async def is_subscribed(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool:
    """Checks if a user is subscribed to ALL required channels."""
    unsubscribed = await check_subscriptions(context, user_id)
    return len(unsubscribed) == 0

async def require_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Checks subscription and sends prompt if not subscribed.
    Returns True if subscribed, False otherwise.
    """
    if not update.effective_user:
        return False
        
    user_id = update.effective_user.id
    unsubscribed = await check_subscriptions(context, user_id)
    
    if unsubscribed:
        # Get language
        user_data = get_user(user_id)
        lang = user_data['language'] if user_data else 'ar'
        s = STRINGS.get(lang, STRINGS['ar'])
        
        # Use message or callback_query to reply
        target = update.message or update.callback_query
        await send_force_join_prompt(target, unsubscribed, s)
        return False
        
    return True

async def send_force_join_prompt(query_or_message, unsubscribed_channels, lang_strings):
    keyboard = []
    
    # Show only the FIRST channel in the list
    first_channel = unsubscribed_channels[0]
    
    # Clean the @ for the URL
    clean_channel = first_channel.replace("@", "")
    channel_url = f"https://t.me/{clean_channel}"
    
    keyboard.append([InlineKeyboardButton(lang_strings['BTN_JOIN_CHANNEL'], url=channel_url)])
    keyboard.append([InlineKeyboardButton(lang_strings['BTN_VERIFY_SUB'], callback_data="verify_sub")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Display only the first channel
    msg_text = lang_strings['FORCE_JOIN_MSG'].format(channels=first_channel)
    
    # Handle callback query vs message
    if hasattr(query_or_message, "reply_text"):
        return await query_or_message.reply_text(
            msg_text,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
    else:
        # If it's a callback query, it's safer to always reply to the message for a "fresh" feel
        return await query_or_message.message.reply_text(
            msg_text,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )



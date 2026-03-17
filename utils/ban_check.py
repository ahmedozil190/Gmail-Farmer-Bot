from telegram import Update
from telegram.ext import ContextTypes
from database import get_user
from strings import STRINGS

async def is_banned(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Check if the user is banned. If so, send a message and return True."""
    user_id = update.effective_user.id
    user_data = get_user(user_id)
    
    if user_data and user_data['status'] == 'banned':
        lang = user_data['language'] if user_data else 'ar'
        # Check if we have a banned message, otherwise use a default
        s = STRINGS.get(lang, STRINGS['ar'])
        msg = "❌ <b>عذراً، تم حظرك من استخدام البوت.</b>" if lang == 'ar' else "❌ <b>Sorry, you have been banned from using this bot.</b>"
        
        await update.message.reply_text(msg, parse_mode="HTML")
        return True
    
    return False

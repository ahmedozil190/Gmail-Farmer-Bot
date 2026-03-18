from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from database import get_user
from keyboards import main_menu
from strings import STRINGS
from config import SUPPORT_LINK
from utils.ban_check import is_banned

async def support_handler_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """💬 المساعدة — show help info."""
    from utils.subscription import require_subscription
    if not await require_subscription(update, context):
        return
    if await is_banned(update, context):
        return
    user_id = update.effective_user.id
    user_data = get_user(user_id)
    lang = user_data['language'] if user_data else 'ar'
    
    s = STRINGS.get(lang, STRINGS['ar'])
    msg = s['SUPPORT_MSG'].format(link=SUPPORT_LINK)

    await update.message.reply_text(
        msg,
        parse_mode="HTML",
        reply_markup=main_menu(lang),
    )

support_handler = MessageHandler(filters.Regex(r"^(💬 Help|💬 المساعدة)$"), support_handler_fn)

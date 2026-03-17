from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from database import get_user
from keyboards import main_menu
from strings import STRINGS


async def myid_handler_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """🪪 عرض الأيدي ID — show user info."""
    user_id = update.effective_user.id
    user_data = get_user(user_id)
    lang = user_data['language'] if user_data else 'ar'
    s = STRINGS.get(lang, STRINGS['ar'])
    
    user = update.effective_user
    await update.message.reply_text(
        f"{s['MYID_TITLE']}"
        f"{s['MYID_NAME'].format(name=user.full_name)}"
        f"{s['MYID_USER'].format(user=user.username or 'N/A')}"
        f"{s['MYID_ID'].format(id=user.id)}",
        parse_mode="HTML",
        reply_markup=main_menu(lang),
    )


myid_handler = MessageHandler(filters.Regex(r"^(🪪 عرض الأيدي ID|🪪 Show ID)$"), myid_handler_fn)

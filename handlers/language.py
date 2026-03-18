from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from database import get_user, update_user_language
from keyboards import main_menu, language_keyboard
from strings import STRINGS
from utils.ban_check import is_banned


async def language_btn_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """User clicked 'Language' button."""
    if await is_banned(update, context):
        return
    user = get_user(update.effective_user.id)
    lang = user['language'] if user else 'ar'
    s = STRINGS.get(lang, STRINGS['ar'])
    
    context.user_data['parent_menu'] = 'settings'
    await update.message.reply_text(
        s['LANG_MSG'],
        reply_markup=language_keyboard(lang)
    )


async def change_lang_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """User selected a specific language."""
    text = update.message.text
    user_id = update.effective_user.id
    
    if "العربية" in text:
        new_lang = 'ar'
    elif "English" in text:
        new_lang = 'en'
    else:
        return

    update_user_language(user_id, new_lang)
    
    # Send welcome messages in new language to confirm
    s = STRINGS[new_lang]
    await update.message.reply_text(
        s['START_MSG_1'],
        parse_mode="HTML"
    )
    await update.message.reply_text(
        s['START_MSG_2'],
        reply_markup=main_menu(new_lang),
        parse_mode="HTML"
    )

# Filters for the language buttons
language_handler = MessageHandler(filters.Regex(r"^🌐\s*(اللغة|Language)$"), language_btn_handler)
select_lang_handler = MessageHandler(filters.Regex(r"(🇸🇦 العربية|العربية 🇸🇦|🇺🇸 English)"), change_lang_handler)

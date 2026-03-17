import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from database import init_db
from handlers.start import start_handler
from handlers.tasks import tasks_conv_handler
from handlers.wallet import balance_handler, history_handler, my_accounts_handler, unified_back_handler
from handlers.support import support_handler, support_handler_fn
from handlers.withdraw import withdraw_conv_handler
from handlers.referral import (
    referral_handler, referral_link_handler, 
    referral_stats_handler, referral_list_handler
)
from handlers.settings import settings_handler, currency_handler, select_currency_handler
from handlers.language import language_handler, select_lang_handler
from handlers.admin import admin_handlers

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():
    # Initialise database
    init_db()
    logger.info("✅ Database initialised.")

    app = Application.builder().token(BOT_TOKEN).build()

    # ── Conversation handlers (must be registered BEFORE plain message handlers)
    app.add_handler(tasks_conv_handler)
    app.add_handler(withdraw_conv_handler)

    # ── Command handlers
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("support", support_handler_fn))

    # ── Plain button handlers
    app.add_handler(balance_handler)
    app.add_handler(history_handler)
    app.add_handler(my_accounts_handler)
    app.add_handler(referral_handler)
    app.add_handler(referral_link_handler)
    app.add_handler(referral_stats_handler)
    app.add_handler(referral_list_handler)
    app.add_handler(settings_handler)
    app.add_handler(currency_handler)
    app.add_handler(select_currency_handler)
    app.add_handler(language_handler)
    app.add_handler(select_lang_handler)
    app.add_handler(support_handler)
    app.add_handler(unified_back_handler)

    # ── Admin commands
    for handler in admin_handlers:
        app.add_handler(handler)

    # ── Event Loop Setup (Fix for Python 3.14+) ──────────────────────────────
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    logger.info("🚀 Bot is running…")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()

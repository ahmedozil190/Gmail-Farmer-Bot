import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ── Bot Credentials ──────────────────────────────────────────────────────────
BOT_TOKEN  = os.getenv("BOT_TOKEN",  "8634536031:AAFwZKu3x_jBgyCW4u673zC73VGwWT7pZW4")
ADMIN_ID   = int(os.getenv("ADMIN_ID", "7142953055"))

# ── Business Settings ────────────────────────────────────────────────────────
BOT_NAME       = os.getenv("BOT_NAME",      "Gmail Store 🇪🇬")
GMAIL_PRICE    = float(os.getenv("GMAIL_PRICE",   "0.20"))   # USD per Gmail
MIN_WITHDRAW   = float(os.getenv("MIN_WITHDRAW",  "0.20"))   # Default USD minimum (Legacy)
BASE_CURRENCY  = "USD"
REFERRAL_BONUS = float(os.getenv("REFERRAL_BONUS", "0.01")) # USD bonus per referral task
SUPPORT_LINK   = os.getenv("SUPPORT_LINK", "@A_M_E_11")
EMAILS_CHANNEL_ID = os.getenv("EMAILS_CHANNEL_ID", "-1003857910149")
WITHDRAWALS_CHANNEL_ID = os.getenv("WITHDRAWALS_CHANNEL_ID", "-1003805740955")

# ── Payment Methods ──────────────────────────────────────────────────────────
PAYMENT_METHODS = [
    "💳 Vodafone Cash",
    "🟡 Binance",
    "🟢 USDT (BEP20)",
    "💎 TRX (TRC20)",
]

MIN_WITHDRAW_METHODS_USD = {
    "💳 Vodafone Cash": float(os.getenv("MIN_WITHDRAW_VODAFONE", "0.20")),
    "🟡 Binance":       float(os.getenv("MIN_WITHDRAW_BINANCE", "0.20")),
    "🟢 USDT (BEP20)":  float(os.getenv("MIN_WITHDRAW_USDT", "0.10")),
    "💎 TRX (TRC20)":   float(os.getenv("MIN_WITHDRAW_TRX", "0.30")),
    "DEFAULT":          float(os.getenv("MIN_WITHDRAW", "0.20"))
}

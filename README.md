# Gmail Store Bot 🇪🇬

بوت تلجرام لشراء حسابات Gmail من المستخدمين.

---

## ⚡ تشغيل البوت

### 1. تثبيت Python
تأكد من تثبيت Python 3.10 أو أحدث.

### 2. تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 3. إعداد ملف البيئة
انسخ `.env.example` إلى `.env` وأضف بياناتك:
```bash
copy .env.example .env
```

افتح ملف `.env` وضع:
```
BOT_TOKEN=8634536031:AAFwZKu3x_jBgyCW4u673zC73VGwWT7pZW4
ADMIN_ID=7142953055
GMAIL_PRICE=10
MIN_WITHDRAW=20
REFERRAL_BONUS=2
```

### 4. تشغيل البوت
```bash
python bot.py
```

---

## 📋 ميزات البوت

| الميزة | الوصف |
|--------|-------|
| 📋 المهام | إرسال حسابات Gmail للبيع |
| 💰 المحفظة | عرض الرصيد المتاح والمعلق |
| 📤 السحب | طلب سحب الأرباح |
| ⏳ الأموال المعلقة | حسابات قيد المراجعة |
| 🔗 الإحالة | رابط إحالة مخصص + 2 جنيه لكل إحالة |
| 🪪 عرض الأيدي ID | معرفة الـ Telegram ID |

---

## 🛠 أوامر الأدمن

| الأمر | الوظيفة |
|-------|---------|
| `/admin` | لوحة التحكم |
| `/pending` | الطلبات المعلقة |
| `/approve 5` | قبول طلب رقم 5 |
| `/reject 5 السبب` | رفض طلب مع السبب |
| `/withdrawals` | طلبات السحب المعلقة |
| `/paid 3` | تأكيد تنفيذ سحب رقم 3 |
| `/stats` | إحصائيات البوت |
| `/broadcast رسالة` | إرسال رسالة لجميع المستخدمين |

---

## 📂 هيكل المشروع

```
gmail-store-bot/
├── bot.py              ← نقطة البداية
├── config.py           ← الإعدادات
├── database.py         ← قاعدة البيانات SQLite
├── keyboards.py        ← لوحات المفاتيح
├── handlers/
│   ├── start.py        ← أمر /start
│   ├── tasks.py        ← إرسال حسابات Gmail
│   ├── wallet.py       ← المحفظة والأموال المعلقة
│   ├── withdraw.py     ← السحب
│   ├── referral.py     ← الإحالة
│   ├── myid.py         ← عرض الـ ID
│   └── admin.py        ← لوحة الأدمن
├── requirements.txt
└── .env.example
```

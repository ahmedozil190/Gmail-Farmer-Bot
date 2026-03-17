# Translation strings for Gmail Store Bot

STRINGS = {
    'ar': {
        'START_MSG_1': (
            "🎉 مرحباً بك في أسهل وأسرع طريقة للربح! 💰\n\n"
            "✨ ابدأ رحلتك نحو الربح الآن ✨"
        ),
        'START_MSG_2': "🎯 اختر زر المهام لتبدأ رحلتك! 🚀",
        
        # Main Menu Buttons
        'BTN_TASKS': "➕ تسجيل إيميل جديد",
        'BTN_MYACCOUNTS': "📂 حساباتي",
        'BTN_BALANCE': "💰 الرصيد",
        'BTN_REFERRAL': "👥 إحالاتي",
        'BTN_SETTINGS': "⚙️ الإعدادات",
        'BTN_CURRENCY': "💵 العملة",
        'BTN_LANG': "🌐 اللغة",
        'BTN_HELP': "💬 المساعدة",
        'BTN_BACK': "🔙 رجوع",
        
        # Balance Menu Buttons
        'BTN_PAYOUT': "💳 سحب",
        'BTN_HISTORY': "📜 سجل العمليات",
        
        # Balance
        'BALANCE_TITLE': "💰 <b>رصيدك</b>\n\n",
        'BALANCE_INFO_ONLY': (
            "الرصيد: <b>{balance:.2f}$</b>\n"
            "معلق: <b>{pending:.2f}$</b>\n"
        ),
        'BALANCE_INFO_DUAL': (
            "الرصيد: <b>{balance_text}</b>\n"
            "معلق: <b>{hold_text}</b>\n"
        ),
        'WALLET_STATS': "📊 <b>إحصائياتك</b>\n• حسابات مقبولة:  {approved}\n• حسابات مرفوضة: {rejected}",
        
        
        # Tasks
        'TASKS_TITLE': "📋 <b>المهام</b>\n\n",
        'TASKS_PRICE': "💵 السعر لكل حساب: <b>{price}</b>\n",
        'TASKS_STATS': "✅ حسابات مقبولة: <b>{approved}</b>\n⏳ في الانتظار: <b>{pending}</b>\n\n",
        'TASKS_PROMPT_EMAIL': "📨 أرسل لي عنوان Gmail الذي تريد بيعه\n<i>مثال: example@gmail.com</i>",
        'TASKS_ERROR_GMAIL': "⚠️ يرجى إرسال عنوان Gmail صحيح!\nمثال: example@gmail.com",
        'TASKS_PROMPT_PWD': "✅ تم استلام الإيميل: <code>{email}</code>\n\n🔑 الآن أرسل كلمة المرور للحساب:",
        'TASKS_SUCCESS': (
            "🎉 <b>تم إرسال الحساب بنجاح!</b>\n\n"
            "📧 الإيميل: <code>{email}</code>\n"
            "🔢 رقم الطلب: <b>#{sub_id}</b>\n\n"
            "⏳ سيتم مراجعة الحساب قريباً وإضافة {price_text} لمحفظتك عند القبول."
        ),
        'PROCESS_CANCELLED': "❌ تم إلغاء العملية.",
        'ERROR_RETRY': "❌ حدث خطأ، ابدأ من جديد.",
        
        # New Gmail Task Flow
        'TASKS_INSTRUCTIONS': (
            "📱 <b>مهمة إنشاء جيميل</b> ⛳️\n\n"
            "📋 <b>التعليمات</b> 🥊\n\n"
            "🔑 كلمة المرور الموحدة ☜ <code>Aa612003@\u200e</code>\n\n"
            "📱 يجب إنشاء الحساب من الهاتف فقط\n"
            "👤 استخدم أي اسم أجنبي 💁‍♂️\n\n"
            "📧 استخدم كلمة المرور الموحدة المذكورة أعلاه 🕺\n\n"
            "⚠️ ستحصل على المكافأة بعد موافقة الأدمن 💸\n\n"
            "💡 بعد إنشاء الحساب، اضغط \"متابعة\" لإدخال الإيميل 📲\n\n"
            "🕐 خذ وقتك - لا يوجد حد زمني لهذه المهمة ⏳"
        ),
        'TASKS_STEPS': (
            "📱 <b>خطوات إكمال هذه المهمة:</b>\n\n"
            "1️⃣ أنشئ حساب جيميل باستخدام كلمة المرور أعلاه\n"
            "2️⃣ اضغط زر \"متابعة\" أدناه\n"
            "3️⃣ أرسل عنوان الجيميل الجديد\n"
            "4️⃣ انتظر موافقة الأدمن\n\n"
            "💰 ستحصل على مكافأتك بعد الموافقة!\n\n"
            "❌ إذا لم تتمكن من إكمال المهمة، يرجى إلغاؤها"
        ),
        'TASKS_PROMPT_EMAIL_ONLY': (
            "✅ ممتاز! الآن أرسل عنوان الجيميل الذي أنشأته:\n\n"
            "💡 مثال: <code>yourname@gmail.com</code>\n\n"
            "⚠️ تأكد من إرسال عنوان الإيميل فقط!"
        ),
        'TASKS_SUCCESS_ONLY': (
            "✅ <b>ممتاز! تم إرسال حساب الجيميل للمراجعة!</b>\n\n"
            "💰 ستحصل على مكافأتك بعد موافقة الأدمن\n"
            "📞 إذا كان لديك أي استفسار، تواصل مع الدعم"
        ),
        'BTN_CONTINUE': "متابعة ✅",
        'BTN_CANCEL_TASK': "إلغاء المهمة ❌",
        'MSG_TASK_CANCELLED': "✅ تم إلغاء المهمة",
        
        # Withdraw
        'WITHDRAW_LOW_BALANCE': (
            "❌ <b>رصيد غير كافٍ.</b> لا يمكنك طلب السحب في الوقت الحالي.\n\n"
            "{balance_info}\n\n"
            "يجب أن يكون رصيدك النشط أكبر من <b>$0</b> لطلب السحب."
        ),
        'WITHDRAW_TITLE': "📤 <b>طلب سحب</b>\n\n",
        'WITHDRAW_AVAIL': "💰 رصيدك المتاح: <b>{balance_text}</b>\n\n",
        'WITHDRAW_METHOD_PROMPT': "اختر طريقة الاستلام:",
        'WITHDRAW_AMOUNT_PROMPT': "✅ الطريقة: <b>{method}</b>\n\n💵 أدخل المبلغ المراد سحبه (الحد الأدنى {min_w:.2f}$، المتاح {balance:.2f}$):",
        'WITHDRAW_ERROR_NUM': "⚠️ أدخل رقمًا صحيحًا.",
        'WITHDRAW_ERROR_MIN': "⚠️ الحد الأدنى للسحب {min_w:.2f}$.",
        'WITHDRAW_ERROR_MAX': "⚠️ المبلغ يتجاوز رصيدك ({balance:.2f}$).",
        'WITHDRAW_WALLET_PROMPT': "📝 أدخل {label}:",
        'WITHDRAW_SUCCESS': (
            "✅ <b>تم إرسال طلب السحب!</b>\n\n"
            "💵 المبلغ: <b>{amount_text}</b>\n"
            "💳 الطريقة: <b>{method}</b>\n"
            "🏦 العنوان: <code>{wallet}</code>\n\n"
            "⏳ سيتم تحويل المبلغ خلال 24 ساعة."
        ),
        'WITHDRAW_PAID': (
            "✅ <b>تم ارسال طلب السحب!</b>\n\n"
            "💵 المبلغ: <b>{amount_text}</b>\n"
            "💳 الطريقة: <b>{method}</b>\n"
            "📝 العنوان: <code>{wallet}</code>\n\n"
            "شكراً لعملك معنا! استمر في الإنجاز 🚀"
        ),
        'WITHDRAW_REJECTED': (
            "❌ <b>تم رفض طلب السحب</b>\n\n"
            "💵 المبلغ: <b>{amount_text}</b>\n"
            "📝 العنوان: <code>{wallet}</code>\n"
            "⚠️ السبب: <b>حدث خطأ تواصل مع الدعم</b>\n\n"
            "🥊 لا تيأس! استمر في العمل لتحقيق المزيد من الأرباح 💰"
        ),
        
        # History & Accounts
        'HISTORY_EMPTY': "لا يوجد سجل عمليات حالياً.",
        'MY_ACCOUNTS_TITLE': "📂 <b>حساباتي</b>\n",
        'MY_ACCOUNTS_EMPTY': "لا توجد حسابات مسجلة حالياً.",
        'SUPPORT_MSG': "💬 <b>المساعدة والدعم الفني</b>\n\nللتحدث مع الدعم الفني: {link}",

        # Wallet Labels
        'LBL_WALLET_VODAFONE': "رقم فودافون كاش",
        'LBL_WALLET_BINANCE': "Binance Pay ID أو UID",
        'LBL_WALLET_USDT': "عنوان محفظة USDT (BEP20)",
        'LBL_WALLET_TRX': "عنوان محفظة TRX (TRC20)",
        'LBL_WALLET_GENERIC': "عنوان المحفظة",
        
        # Referral
        'REF_MSG': (
            "📎 <b>نظام الإحالة</b>\n\n"
            "💰 احصل على {bonus_text} عن كل مهمة جيميل يكملها أصدقاؤك!\n\n"
            "📊 <b>إحصائياتك:</b>\n"
            "👥 الأصدقاء المدعوين: <b>{invited}</b>\n"
            "🎯 إجمالي المهام: <b>{tasks}</b>\n"
            "💰 إجمالي الأرباح: <b>{profit_text}</b>\n\n"
            "💡 أصدقاؤك يعملون = أنت تربح!\n"
            "✨ إمكانية ربح غير محدودة!"
        ),
        'REF_STATS_MSG': (
            "📊 <b>إحصائيات الإحالة:</b>\n\n"
            "👥 إجمالي المدعوين: <b>{invited}</b>\n"
            "✅ الإحالات النشطة: <b>{active}</b>\n"
            "🎯 إجمالي المهام المكتملة: <b>{tasks}</b>\n"
            "💰 إجمالي الأرباح: <b>{profit_text}</b>\n"
            "💵 المكافأة لكل مهمة: <b>{bonus_text}</b>\n\n"
            "🔗 كود الإحالة: <code>{ref_id}</code>\n\n"
            "💡 تحصل على {bonus_text} عن كل مهمة جيميل يكملها أصدقاؤك!\n"
            "✨ كلما عملوا أكثر، ربحت أكثر!"
        ),
        'REF_LINK_DETAILS': (
            "🔗 <b>رابط الإحالة الخاص بك:</b>\n\n"
            "{link}\n\n"
            "📋 انسخ هذا الرابط وشاركه مع أصدقائك\n"
            "💰 ستحصل على {bonus_text} عن كل مهمة جيميل يكملونها!\n\n"
            "🎯 كود الإحالة: <code>{ref_id}</code>\n\n"
            "💡 كلما أكملوا مهام أكثر، ربحت أكثر!\n"
            "✨ إمكانية ربح غير محدودة!\n\n"
            "👆 اضغط على الرابط أعلاه لتجربته!"
        ),
        'BTN_REF_LINK': "🔗 رابط الإحالة",
        'BTN_REF_STATS': "📊 إحصائيات الإحالة",
        'BTN_REF_LIST': "👥 قائمة الإحالات",
        'BTN_BACK_MAIN': "🔙 العودة للقائمة الرئيسية",
        'REF_LIST_EMPTY': (
            "👥 <b>قائمة الإحالات:</b>\n\n"
            "📭 لم تقم بإحالة أي شخص بعد\n\n"
            "💡 شارك رابط الإحالة لتبدأ الربح!"
        ),
        'REF_LIST_HEADER': "👥 <b>إحالاتك ({count}):</b>\n\n",
        'REF_LIST_ITEM': (
            "{index}. {name}\n"
            "   {status_icon} {status_text} | 💰 {earned_text} | 📅 {date}\n"
            "━━━━━━━━━━━━━━━\n"
        ),
        'REF_STATUS_PENDING': "معلق",
        'REF_STATUS_EARNED': "تم الكسب",
        'REF_EARNED_NONE': "لم يتم الكسب بعد",
        
        # Admin Commands
        'ADMIN_ONLY': "⛔ هذا الأمر للأدمن فقط.",
        'ADMIN_PANEL_TITLE': "🛠 <b>لوحة التحكم</b>\n\n",
        'ADMIN_PANEL_STATS': (
            "👥 إجمالي المستخدمين:   <b>{total}</b>\n"
            "✅ حسابات مقبولة:      <b>{approved}</b>\n"
            "⏳ حسابات معلقة:       <b>{pending}</b>\n"
            "💸 طلبات سحب معلقة:    <b>{pending_w}</b>\n"
            "💰 إجمالي المدفوع:     <b>{paid_text}</b>\n\n"
            "🌐 <b>لوحة تحكم الويب:</b>\n"
            "للكمبيوتر: http://127.0.0.1:5000\n"
            "للهاتف (نفس الواي فاي): http://192.168.1.5:5000\n\n"
            "الأوامر:\n"
            "/pending — الطلبات المعلقة\n"
            "/withdrawals — طلبات السحب\n"
            "/stats — إحصائيات مفصلة\n"
            "/broadcast رسالتك — إرسال للجميع"
        ),
        'ADMIN_PENDING_NONE': "✅ لا توجد طلبات معلقة.",
        'ADMIN_PENDING_HEADER': "📋 <b>الطلبات المعلقة ({count})</b>\n",
        'ADMIN_PENDING_ITEM': (
            "• <b>#{id}</b> | user:<code>{user_id}</code>\n"
            "  📧 <code>{gmail}</code>\n"
            "  🔑 <code>{pwd}</code>\n"
            "  📅 {date}\n"
            "  👉 /approve {id}  |  /reject {id} السبب"
        ),
        'ADMIN_APPROVE_USAGE': "استخدام: /approve <id>",
        'ADMIN_APPROVE_ERROR_ID': "⚠️ أدخل رقم طلب صحيح.",
        'ADMIN_APPROVE_NOT_FOUND': "❌ الطلب #{id} غير موجود أو تم معالجته مسبقاً.",
        'ADMIN_APPROVE_SUCCESS': (
            "✅ تم قبول الطلب <b>#{id}</b> ✅\n"
            "💰 تم إضافة المبلغ لمحفظة المستخدم."
        ),
        'ADMIN_REJECT_USAGE': "استخدام: /reject <id> [السبب]",
        'ADMIN_REJECT_SUCCESS': "🚫 تم رفض الطلب <b>#{id}</b>\nالسبب: {reason}",
        'ADMIN_W_PENDING_NONE': "✅ لا توجد طلبات سحب معلقة.",
        'ADMIN_W_PENDING_HEADER': "💸 <b>طلبات السحب المعلقة ({count})</b>\n",
        'ADMIN_W_PENDING_ITEM': (
            "• <b>#{id}</b> | user:<code>{user_id}</code>\n"
            "  💵 {amount_text}  |  {method}\n"
            "  🏦 <code>{wallet}</code>\n"
            "  👉 /paid {id}"
        ),
        'ADMIN_PAID_USAGE': "استخدام: /paid <id>",
        'ADMIN_PAID_SUCCESS': "✅ تم تأكيد السحب #{id} كمكتمل.",
        'ADMIN_STATS_TITLE': "📊 <b>الإحصائيات الكاملة</b>\n\n",
        'ADMIN_STATS_BODY': (
            "👥 المستخدمون: <b>{total}</b>\n"
            "✅ مقبول: <b>{approved}</b>\n"
            "⏳ معلق: <b>{pending}</b>\n"
            "💰 مدفوع: <b>{paid_text}</b>"
        ),
        'ADMIN_BROADCAST_USAGE': "استخدام: /broadcast رسالتك هنا",
        'ADMIN_BROADCAST_SUCCESS': "📢 <b>تم الإرسال</b>\n✅ نجح: {sent} | ❌ فشل: {failed}",
        
        # Admin Notifications (New Gmail/Withdraw)
        'ADMIN_NOTIFY_GMAIL': (
            "📬 <b>طلب جديد #{sub_id}</b>\n\n"
            "👤 المستخدم: {user_name} (<code>{user_id}</code>)\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "🔑 Password: <code>{pwd}</code>\n"
            "🌐 Language: {u_lang}\n\n"
            "للقبول: /approve {sub_id}\n"
            "للرفض: /reject {sub_id} السبب"
        ),
        'ADMIN_NOTIFY_WITHDRAW': (
            "💸 <b>طلب سحب جديد #{wid}</b>\n\n"
            "👤 المستخدم: {user_name} (<code>{user_id}</code>)\n"
            "💵 المبلغ: <b>{amount_text}</b>\n"
            "💳 الطريقة: {method}\n"
            "🏦 العنوان: <code>{wallet}</code>\n"
            "🌐 Language: {u_lang}\n\n"
            "للتأكيد: /paid {wid}"
        ),
        'NOTIFY_USER_APPROVE': (
            "🎉 <b>تهانينا!</b> تم قبول حسابك!\n\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "💵 تم إضافة <b>{price_text}</b> لمحفظتك ✅"
        ),
        'NOTIFY_USER_REJECT': (
            "❌ <b>تم رفض حسابك</b>\n\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "📝 السبب: {reason}\n\n"
            "يمكنك إرسال حساب آخر."
        ),
        'NOTIFY_USER_PAID': (
            "💸 <b>تم سحب رصيدك بنجاح!</b>\n\n"
            "💵 المبلغ: <b>{amount_text}</b>\n"
            "✅ تم تحويل المبلغ إلى حسابك. شكراً لعملك معنا!"
        ),
        'LBL_CURRENCY_EGP': "جنيه",
        'DEF_REASON': "غير محدد",
        
        # Balance Menu Buttons
        'SETTINGS_MSG': "⚙️ <b>الإعدادات</b>\n\nاختر الخيار الذي تريد تعديله:",
        
        # Currency
        'CURRENCY_MSG': (
            "The main currency in the bot is <b>USD - US dollar</b>, however, you can choose "
            "one of the 174 currencies that will be used for visual display\n\n"
            "❗️ The currency you choose affects only the visual display, it can always be changed in settings"
        ),
        'CURRENCY_SET_SUCCESS': "✅ تم ضبط العملة بنجاح إلى: <b>{currency}</b>",
        'BTN_NEXT_PAGE': "➡️ الصفحة التالية",
        'BTN_PREV_PAGE': "⬅️ الصفحة السابقة",
        
        # Language
        'LANG_MSG': "🌐 اختر اللغة / Choose Language:",
    },
    'en': {
        'START_MSG_1': (
            "🎉 Welcome to the easiest and fastest way to earn! 💰\n\n"
            "✨ Start your journey to profit now ✨"
        ),
        'START_MSG_2': "🎯 Choose the Tasks button to start your journey! 🚀",
        
        # Main Menu Buttons
        'BTN_TASKS': "➕ Register a new Gmail",
        'BTN_MYACCOUNTS': "📂 My accounts",
        'BTN_BALANCE': "💰 Balance",
        'BTN_REFERRAL': "👥 My referrals",
        'BTN_SETTINGS': "⚙️ Settings",
        'BTN_CURRENCY': "💵 Currency",
        'BTN_LANG': "🌐 Language",
        'BTN_HELP': "💬 Help",
        'BTN_BACK': "🔙 Back",
        
        # Balance Menu Buttons
        'BTN_PAYOUT': "💳 Payout",
        'BTN_HISTORY': "📜 Balance history",
        
        # Balance
        'BALANCE_TITLE': "💰 <b>Balance</b>\n\n",
        'BALANCE_INFO_ONLY': (
            "Balance: <b>{balance:.2f}$</b>\n"
            "Hold: <b>{pending:.2f}$</b>\n"
        ),
        'BALANCE_INFO_DUAL': (
            "Balance: <b>{balance_text}</b>\n"
            "Hold: <b>{hold_text}</b>\n"
        ),
        'WALLET_STATS': "📊 <b>Your Stats</b>\n• Approved accounts:  {approved}\n• Rejected accounts: {rejected}",
        
        
        # Tasks
        'TASKS_TITLE': "📋 <b>Tasks</b>\n\n",
        'TASKS_PRICE': "💵 Price per account: <b>{price}</b>\n",
        'TASKS_STATS': "✅ Approved: <b>{approved}</b>\n⏳ Pending: <b>{pending}</b>\n\n",
        'TASKS_PROMPT_EMAIL': "📨 Send me the Gmail address you want to sell\n<i>Example: example@gmail.com</i>",
        'TASKS_ERROR_GMAIL': "⚠️ Please send a valid Gmail address!\nExample: example@gmail.com",
        'TASKS_PROMPT_PWD': "✅ Email received: <code>{email}</code>\n\n🔑 Now send the account password:",
        'TASKS_SUCCESS': (
            "🎉 <b>Account submitted successfully!</b>\n\n"
            "📧 Email: <code>{email}</code>\n"
            "🔢 Order ID: <b>#{sub_id}</b>\n\n"
            "⏳ Account will be reviewed soon and {price_text} will be added to your wallet upon approval."
        ),
        'PROCESS_CANCELLED': "❌ Process cancelled.",
        'ERROR_RETRY': "❌ An error occurred, start over.",

        # New Gmail Task Flow
        'TASKS_INSTRUCTIONS': (
            "📱 <b>Gmail Creation Task</b> ⛳️\n\n"
            "📋 <b>Instructions</b> 🥊\n\n"
            "🔑 Unified Password ☜ <code>Aa612003@</code>\n\n"
            "📱 Account must be created from phone only\n"
            "👤 Use any foreign name 💁‍♂️\n\n"
            "📧 Use the unified password mentioned above 🕺\n\n"
            "⚠️ You will receive the reward after admin approval 💸\n\n"
            "💡 After creating the account, press \"Continue\" to enter the email 📲\n\n"
            "🕐 Take your time - there is no time limit for this task ⏳"
        ),
        'TASKS_STEPS': (
            "📱 <b>Steps to complete this task:</b>\n\n"
            "1️⃣ Create a Gmail account using the password above\n"
            "2️⃣ Press the \"Continue\" button below\n"
            "3️⃣ Send the new Gmail address\n"
            "4️⃣ Wait for admin approval\n\n"
            "💰 You will get your reward after approval!\n\n"
            "❌ If you cannot complete the task, please cancel it"
        ),
        'TASKS_PROMPT_EMAIL_ONLY': (
            "✅ Excellent! Now send the Gmail address you created:\n\n"
            "💡 Example: <code>yourname@gmail.com</code>\n\n"
            "⚠️ Make sure to send the email address only!"
        ),
        'TASKS_SUCCESS_ONLY': (
            "✅ <b>Excellent! The Gmail account has been submitted for review!</b>\n\n"
            "💰 You will receive your reward after admin approval\n"
            "📞 If you have any questions, contact support"
        ),
        'BTN_CONTINUE': "Continue ✅",
        'BTN_CANCEL_TASK': "Cancel Task ❌",
        'MSG_TASK_CANCELLED': "✅ Task cancelled",
        
        # Withdraw
        'WITHDRAW_LOW_BALANCE': (
            "❌ <b>Insufficient active balance.</b> You cannot request a payout at this time.\n\n"
            "{balance_info}\n\n"
            "Your active balance must be greater than <b>$0</b> to request a withdrawal."
        ),
        'WITHDRAW_TITLE': "📤 <b>Withdrawal Request</b>\n\n",
        'WITHDRAW_AVAIL': "💰 Available Balance: <b>{balance:.2f}$</b>\n\n",
        'WITHDRAW_METHOD_PROMPT': "Choose payment method:",
        'WITHDRAW_AMOUNT_PROMPT': "✅ Method: <b>{method}</b>\n\n💵 Enter the amount to withdraw (Min {min_w:.2f}$, Available {balance:.2f}$):",
        'WITHDRAW_ERROR_NUM': "⚠️ Enter a valid number.",
        'WITHDRAW_ERROR_MIN': "⚠️ Minimum withdrawal is {min_w:.2f}$.",
        'WITHDRAW_ERROR_MAX': "⚠️ Amount exceeds your balance ({balance:.2f}$).",
        'WITHDRAW_WALLET_PROMPT': "📝 Enter your {label}:",
        'WITHDRAW_SUCCESS': (
            "✅ <b>Withdrawal request sent!</b>\n\n"
            "💵 Amount: <b>{amount_text}</b>\n"
            "💳 Method: <b>{method}</b>\n"
            "🏦 Address: <code>{wallet}</code>\n\n"
            "⏳ Payment will be processed within 24 hours."
        ),
        'WITHDRAW_PAID': (
            "✅ <b>Withdrawal paid!</b>\n\n"
            "💵 Amount: <b>{amount_text}</b>\n"
            "💳 Method: <b>{method}</b>\n"
            "📝 Address: <code>{wallet}</code>\n\n"
            "Thank you for working with us! Keep it up 🚀"
        ),
        'WITHDRAW_REJECTED': (
            "❌ <b>Withdrawal rejected</b>\n\n"
            "💵 Amount: <b>{amount_text}</b>\n"
            "📝 Address: <code>{wallet}</code>\n"
            "⚠️ Reason: <b>An error occurred, contact support</b>\n\n"
            "🥊 Don't give up! Keep working to earn more rewards 💰"
        ),

        # History & Accounts
        'HISTORY_EMPTY': "No balance history yet.",
        'MY_ACCOUNTS_TITLE': "📂 <b>My accounts</b>\n",
        'MY_ACCOUNTS_EMPTY': "No accounts registered yet.",
        'SUPPORT_MSG': "💬 <b>Help & Tech Support</b>\n\nTo contact support: {link}",

        # Wallet Labels
        'LBL_WALLET_VODAFONE': "Vodafone Cash Number",
        'LBL_WALLET_BINANCE': "Binance Pay ID or UID",
        'LBL_WALLET_USDT': "USDT (BEP20) Wallet Address",
        'LBL_WALLET_TRX': "TRX (TRC20) Wallet Address",
        'LBL_WALLET_GENERIC': "Wallet Address",
        
        # Referral
        'REF_MSG': (
            "📎 <b>Referral System</b>\n\n"
            "💰 Get {bonus_text} for every Gmail task completed by your referred friends!\n\n"
            "📊 <b>Your Stats:</b>\n"
            "👥 Invited friends: <b>{invited}</b>\n"
            "🎯 Total tasks: <b>{tasks}</b>\n"
            "💰 Total profit: <b>{profit_text}</b>\n\n"
            "💡 Your friends work = You earn!\n"
            "✨ Unlimited earning potential!"
        ),
        'REF_STATS_MSG': (
            "📊 <b>Referral Stats:</b>\n\n"
            "👥 Total invited: <b>{invited}</b>\n"
            "✅ Active referrals: <b>{active}</b>\n"
            "🎯 Total tasks completed: <b>{tasks}</b>\n"
            "💰 Total profit: <b>{profit_text}</b>\n"
            "💵 Bonus per task: <b>{bonus_text}</b>\n\n"
            "🔗 Referral code: <code>{ref_id}</code>\n\n"
            "💡 You get {bonus_text} for every Gmail task your friends complete!\n"
            "✨ The more they work, the more you win!"
        ),
        'REF_LINK_DETAILS': (
            "🔗 <b>Your Referral Link:</b>\n\n"
            "{link}\n\n"
            "📋 Copy this link and share it with your friends\n"
            "💰 You'll get {bonus_text} for every Gmail task they complete!\n\n"
            "🎯 Referral Code: <code>{ref_id}</code>\n\n"
            "💡 The more tasks they complete, the more you win!\n"
            "✨ Unlimited earning potential!\n\n"
            "👆 Click the link above to test it!"
        ),
        'BTN_REF_LINK': "🔗 Referral Link",
        'BTN_REF_STATS': "📊 Referral Stats",
        'BTN_REF_LIST': "👥 Referral List",
        'BTN_BACK_MAIN': "🔙 Back to Main Menu",
        'REF_LIST_EMPTY': (
            "👥 <b>Referral List:</b>\n\n"
            "📭 You haven't referred anyone yet\n\n"
            "💡 Share your referral link to start earning!"
        ),
        'REF_LIST_HEADER': "👥 <b>Your Referrals ({count}):</b>\n\n",
        'REF_LIST_ITEM': (
            "{index}. {name}\n"
            "   {status_icon} {status_text} | 💰 {earned_text} | 📅 {date}\n"
            "━━━━━━━━━━━━━━━\n"
        ),
        'REF_STATUS_PENDING': "Pending",
        'REF_STATUS_EARNED': "Earned",
        'REF_EARNED_NONE': "No profit yet",

        # Admin Commands
        'ADMIN_ONLY': "⛔ This command is for admin only.",
        'ADMIN_PANEL_TITLE': "🛠 <b>Admin Panel</b>\n\n",
        'ADMIN_PANEL_STATS': (
            "👥 Total Users:   <b>{total}</b>\n"
            "✅ Approved Tasks:      <b>{approved}</b>\n"
            "⏳ Pending Tasks:       <b>{pending}</b>\n"
            "💸 Pending Withdrawals:    <b>{pending_w}</b>\n"
            "💰 Total Paid:     <b>{paid_text}</b>\n\n"
            "🌐 <b>Web Dashboard:</b>\n"
            "PC: http://127.0.0.1:5000\n"
            "Mobile (Same WiFi): http://192.168.1.5:5000\n\n"
            "Commands:\n"
            "/pending — Pending tasks\n"
            "/withdrawals — Withdrawal requests\n"
            "/stats — Detailed stats\n"
            "/broadcast your message — Send to all users"
        ),
        'ADMIN_PENDING_NONE': "✅ No pending tasks.",
        'ADMIN_PENDING_HEADER': "📋 <b>Pending Tasks ({count})</b>\n",
        'ADMIN_PENDING_ITEM': (
            "• <b>#{id}</b> | user:<code>{user_id}</code>\n"
            "  📧 <code>{gmail}</code>\n"
            "  🔑 <code>{pwd}</code>\n"
            "  📅 {date}\n"
            "  👉 /approve {id}  |  /reject {id} reason"
        ),
        'ADMIN_APPROVE_USAGE': "Usage: /approve <id>",
        'ADMIN_APPROVE_ERROR_ID': "⚠️ Enter a valid ID.",
        'ADMIN_APPROVE_NOT_FOUND': "❌ Task #{id} not found or already processed.",
        'ADMIN_APPROVE_SUCCESS': (
            "✅ Task <b>#{id}</b> approved ✅\n"
            "💰 Amount added to user's wallet."
        ),
        'ADMIN_REJECT_USAGE': "Usage: /reject <id> [reason]",
        'ADMIN_REJECT_SUCCESS': "🚫 Task <b>#{id}</b> rejected\nReason: {reason}",
        'ADMIN_W_PENDING_NONE': "✅ No pending withdrawals.",
        'ADMIN_W_PENDING_HEADER': "💸 <b>Pending Withdrawals ({count})</b>\n",
        'ADMIN_W_PENDING_ITEM': (
            "• <b>#{id}</b> | user:<code>{user_id}</code>\n"
            "  💵 {amount_text}  |  {method}\n"
            "  🏦 <code>{wallet}</code>\n"
            "  👉 /paid {id}"
        ),
        'ADMIN_PAID_USAGE': "Usage: /paid <id>",
        'ADMIN_PAID_SUCCESS': "✅ Withdrawal #{id} marked as paid.",
        'ADMIN_STATS_TITLE': "📊 <b>Global Statistics</b>\n\n",
        'ADMIN_STATS_BODY': (
            "👥 Users: <b>{total}</b>\n"
            "✅ Approved: <b>{approved}</b>\n"
            "⏳ Pending: <b>{pending}</b>\n"
            "💰 Paid: <b>{paid_text}</b>"
        ),
        'ADMIN_BROADCAST_USAGE': "Usage: /broadcast your message here",
        'ADMIN_BROADCAST_SUCCESS': "📢 <b>Broadcast Sent</b>\n✅ Success: {sent} | ❌ Failed: {failed}",

        # Admin Notifications (New Gmail/Withdraw)
        'ADMIN_NOTIFY_GMAIL': (
            "📬 <b>New Submission #{sub_id}</b>\n\n"
            "👤 User: {user_name} (<code>{user_id}</code>)\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "🔑 Password: <code>{pwd}</code>\n"
            "🌐 Language: {u_lang}\n\n"
            "Approve: /approve {sub_id}\n"
            "Reject: /reject {sub_id} reason"
        ),
        'ADMIN_NOTIFY_WITHDRAW': (
            "💸 <b>New Withdrawal #{wid}</b>\n\n"
            "👤 User: {user_name} (<code>{user_id}</code>)\n"
            "💵 Amount: <b>{amount_text}</b>\n"
            "💳 Method: {method}\n"
            "🏦 Address: <code>{wallet}</code>\n"
            "🌐 Language: {u_lang}\n\n"
            "Confirm: /paid {wid}"
        ),
        'NOTIFY_USER_APPROVE': (
            "🎉 <b>Congratulations!</b> Your account was accepted!\n\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "💵 <b>{price_text}</b> has been added to your wallet ✅"
        ),
        'NOTIFY_USER_REJECT': (
            "❌ <b>Your submission was rejected</b>\n\n"
            "📧 Gmail: <code>{gmail}</code>\n"
            "📝 Reason: {reason}\n\n"
            "You can submit another account."
        ),
        'NOTIFY_USER_PAID': (
            "💸 <b>Withdrawal Successful!</b>\n\n"
            "💵 Amount: <b>{amount_text}</b>\n"
            "✅ The amount has been transferred to your account. Thank you for your work!"
        ),
        'LBL_CURRENCY_EGP': "EGP",
        'DEF_REASON': "Not specified",
        
        # Balance Menu Buttons
        'SETTINGS_MSG': "⚙️ <b>Settings</b>\n\nChoose the option you want to modify:",
        
        # Currency
        'CURRENCY_MSG': (
            "The main currency in the bot is <b>USD - US dollar</b>, however, you can choose "
            "one of the 174 currencies that will be used for visual display\n\n"
            "❗️ The currency you choose affects only the visual display, it can always be changed in settings"
        ),
        'CURRENCY_SET_SUCCESS': "✅ Currency successfully set to: <b>{currency}</b>",
        'BTN_NEXT_PAGE': "➡️ Next Page",
        'BTN_PREV_PAGE': "⬅️ Previous Page",
        
        # Language
        'LANG_MSG': "🌐 Choose Language / اختر اللغة:",
    }
}

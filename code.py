from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# بارگذاری توکن از فایل .env
load_dotenv()
BOT_TOKEN = os.getenv("7603187249:AAHSgDa9m0BySOtvnj66navgyLmYbkvzIRI")

# لیست شماره‌ها
phone_numbers = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پیغام خوش‌آمدگویی به کاربر"""
    await update.message.reply_text(
        "سلام! لطفاً شماره‌های خود را یکی یکی ارسال کنید. برای ارسال پیام به همه شماره‌ها، دستور /send را وارد کنید."
    )

async def get_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """دریافت شماره از کاربر"""
    global phone_numbers
    phone = update.message.text.strip()
    
    if len(phone_numbers) >= 500:
        await update.message.reply_text("حداکثر تعداد شماره‌ها (500) ثبت شده است.")
        return
    
    if phone.isdigit() and len(phone) >= 10:  # بررسی فرمت شماره
        phone_numbers.append(phone)
        await update.message.reply_text(f"شماره {phone} ثبت شد. تعداد شماره‌های ثبت‌شده: {len(phone_numbers)}")
    else:
        await update.message.reply_text("لطفاً یک شماره معتبر ارسال کنید.")

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ارسال پیام به شماره‌ها"""
    global phone_numbers
    if not phone_numbers:
        await update.message.reply_text("هیچ شماره‌ای ثبت نشده است!")
        return

    # متنی که ارسال می‌شود
    message = "این یک پیام تست است که توسط ربات ارسال شده است."
    
    for phone in phone_numbers:
        # فرضی: ارسال پیام به شماره‌ها از طریق سرویس دیگر (API یا سرویس پیامک)
        print(f"ارسال پیام به {phone}: {message}")

    await update.message.reply_text(f"پیام برای {len(phone_numbers)} شماره ارسال شد!")
    phone_numbers = []  # پاک کردن لیست شماره‌ها پس از ارسال

# تنظیمات ربات
app = ApplicationBuilder().token(BOT_TOKEN).build()

# هندلرها
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone_number))
app.add_handler(CommandHandler("send", send_message))

if __name__ == "__main__":
    print("ربات در حال اجراست...")
    app.run_polling()

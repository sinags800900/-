from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# توکن بات خود را در اینجا جایگذاری کنید
BOT_TOKEN = '7603187249:AAHSgDa9m0BySOtvnj66navgyLmYbkvzIRI'

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ارسال پیام خوشامدگویی و دکمه‌های بازی"""
    keyboard = [
        [InlineKeyboardButton("شروع بازی", callback_data='start_game')],
        [InlineKeyboardButton("درباره بازی", callback_data='about_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        text="سلام! به بازی تلگرام خوش آمدید. از دکمه‌های زیر استفاده کنید.",
        reply_markup=reply_markup
    )

def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """مدیریت کلیک روی دکمه‌ها"""
    query = update.callback_query
    await query.answer()

    if query.data == 'start_game':
        await query.edit_message_text(
            text="بازی شروع شد! اولین سوال: 2 + 2 چند می‌شود؟",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("4", callback_data='correct_answer')],
                [InlineKeyboardButton("5", callback_data='wrong_answer')]
            ])
        )

    elif query.data == 'about_game':
        await query.edit_message_text(
            text="این یک بازی ساده است که با سوال و جواب کار می‌کند. لذت ببرید!"
        )

    elif query.data == 'correct_answer':
        await query.edit_message_text(
            text="آفرین! درست جواب دادی. سوال بعدی: 3 * 3 چند می‌شود؟",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("9", callback_data='correct_next')],
                [InlineKeyboardButton("6", callback_data='wrong_next')]
            ])
        )

    elif query.data == 'wrong_answer':
        await query.edit_message_text(text="اشتباه جواب دادی! دوباره امتحان کن.")

    elif query.data == 'correct_next':
        await query.edit_message_text(text="تبریک! بازی به پایان رسید.")

    elif query.data == 'wrong_next':
        await query.edit_message_text(text="اشتباه جواب دادی! بازی تمام شد.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

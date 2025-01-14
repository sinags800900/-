const TelegramBot = require('node-telegram-bot-api');

// توکن بات خود را اینجا جایگذاری کنید
const token = '7603187249:AAHSgDa9m0BySOtvnj66navgyLmYbkvzIRI';

// ایجاد یک نمونه از بات
const bot = new TelegramBot(token, { polling: true });

// مدیریت دستور /start
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'سلام! به بازی تلگرام خوش آمدید.', {
    reply_markup: {
      inline_keyboard: [
        [{ text: 'شروع بازی', callback_data: 'start_game' }],
        [{ text: 'درباره بازی', callback_data: 'about_game' }],
      ],
    },
  });
});

// مدیریت کلیک روی دکمه‌ها
bot.on('callback_query', (query) => {
  const chatId = query.message.chat.id;

  if (query.data === 'start_game') {
    bot.sendMessage(chatId, 'بازی شروع شد! اولین سوال: 2 + 2 چند می‌شود؟', {
      reply_markup: {
        inline_keyboard: [
          [{ text: '4', callback_data: 'correct_answer' }],
          [{ text: '5', callback_data: 'wrong_answer' }],
        ],
      },
    });
  } else if (query.data === 'about_game') {
    bot.sendMessage(chatId, 'این یک بازی ساده است که با سوال و جواب کار می‌کند.');
  } else if (query.data === 'correct_answer') {
    bot.sendMessage(chatId, 'آفرین! درست جواب دادی.');
  } else if (query.data === 'wrong_answer') {
    bot.sendMessage(chatId, 'اشتباه جواب دادی! دوباره امتحان کن.');
  }
});

console.log('Bot is running...');

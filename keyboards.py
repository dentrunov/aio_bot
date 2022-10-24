from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')
button_help = KeyboardButton('Нужна помощь?')
button_cur = KeyboardButton('Расписание')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_hi, button_help, button_cur)

button_10A = KeyboardButton('10А')
button_10B = KeyboardButton('10Б')

cur_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_10A, button_10B)

yes_key = KeyboardButton('ДА!!!')
no_key = KeyboardButton('Прости, но нет!')
yes_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(yes_key, no_key)
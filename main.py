from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from tkn import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')
button_help = KeyboardButton('Нужна помощь?')
button_cur = KeyboardButton('/Расписание')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi, button_help, button_cur)

button_10A = KeyboardButton('10А')
button_10B = KeyboardButton('10Б')

cur_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_10A, button_10B)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=greet_kb)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!", reply_markup=greet_kb)

@dp.message_handler(commands=['Расписание'])
async def cur_message(message: types.Message):
    await message.reply("Расписание уроков", reply_markup=cur_kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Я тебя не понимаю')

if __name__ == '__main__':
    executor.start_polling(dp)
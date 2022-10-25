import time, random
import asyncio
import aioschedule

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import keyboards as kb
from tkn import TOKEN, channel_id

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

greetings = ['Всем привет, меня зовут Женя, я ваша новая подруга', 'Хеллоу, мои друзьяшки!', 'Не сдать вам ЕГЭ на сотку', 'Кто сдает ЕГЭ по информатике?']

users = dict()


with open('verbs.txt') as file:
    verbs = file.read().split()
with open('nouns.txt') as file:
    nouns = file.read().split()
with open('adjectives.txt') as file:
    adjectives = file.read().split()

async def on_shutdown(_):
    chat_id = channel_id
    await bot.send_message(chat_id, "Всем пока, я спать")
'''
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.chat_id)
    await message.reply("Привет!", reply_markup=kb.greet_kb)

@dp.message_handler(commands=['help', 'Нужна помощь?'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!", reply_markup=kb.greet_kb)

@dp.message_handler(text='Расписание')
async def cur_message(message: types.Message):
    await message.reply("Расписание уроков", reply_markup=kb.cur_kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Я тебя не понимаю')
'''
async def cmd_test2(message: types.Message):
    await message.reply('<b>Привет, {0}! Я официальный бот твоего любимого чата.</b>\n\
Пока я ничего не умею, но вскоре всему научусь!'.format(message.from_user.first_name),parse_mode="html")

dp.register_message_handler(cmd_test2, commands="helpWiedzmin")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!", reply_markup=kb.greet_kb)

@dp.message_handler()
async def filter_messages(message: types.Message):
    global users
    if "привет" in message.text.lower():
        await message.answer(random.choice(greetings))
    elif "бот" in message.text.lower():
        await message.answer('Привет, я бот\n Мой репозиторий тут https://github.com/dentrunov/aio_bot', reply_markup=kb.greet_kb)
    elif "жека" in message.text.lower():
        await message.answer("хало, как дела, чё как", reply_markup=kb.greet_kb)
    elif "женя" in message.text.lower():
        await message.answer("Эй, привет!!!", reply_markup=kb.greet_kb)
    elif "евгения" in message.text.lower():
        await message.answer("Здравствуйте, как поживаете?", reply_markup=kb.greet_kb)
    elif "помощь" in message.text.lower():
        await message.answer('Ты хочешь об этом поговорить?', reply_markup=kb.yes_kb)
    elif message.text.lower() == "ДА!!!":
        await message.answer(random.choice(greetings), reply_markup=kb.ReplyKeyboardRemove())
    elif message.text.lower() == "Прости, но нет!":
        await message.answer('Не очень-то и хотелось(', reply_markup=kb.ReplyKeyboardRemove())
    elif "расписание" in message.text.lower():
        await message.answer('https://school.mos.ru/')
    else:
        answer = ' '.join([random.choice(adjectives), random.choice(nouns), random.choice(verbs)]).capitalize()+'!'


        await message.answer(answer)
    if not(message.from_user.id in users.keys()):
        await message.answer(f'{message.from_user.first_name} - ты с нами')

    users[message.from_user.id] = [message.from_user.first_name, time.time(), message.chat.id]


async def mess():
    flag = False
    for user in users.keys():

        voices = [f'{users[user][0]} - ты куда пропал?', 'Где все???', 'Скучно без вас :(', 'Я тут одна скучаю...']
        if time.time() - users[user][1] < 600:
            await bot.send_message(users[user][2], random.choice(voices))
            break




async def scheduler():
    aioschedule.every(10).minutes.do(mess)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    chat_id = channel_id
    asyncio.create_task(scheduler())
    await bot.send_message(chat_id, "Привет, я бот\n Мой репозиторий тут https://github.com/dentrunov/aio_bot")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

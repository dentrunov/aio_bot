import time, random
import asyncio
import aioschedule

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards2 as kb
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


users = dict()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if message.from_user.id in users.keys():
        print(users, 1)
    else:
        users[message.from_user.id] = []
    await message.answer("Привет!", reply_markup=kb.greet_kb)


@dp.message_handler(text='Полное расписание')
async def process_cur_command(message: types.Message):
    if not(message.from_user.id in users.keys()):
        await message.answer("Полное расписание", reply_markup=kb.full_cur_kb)
    else:
        print(users)
        await message.answer(class_cur(message.from_user.id), reply_markup=kb.back_kb)


@dp.callback_query_handler(text_contains='button_')
async def process_class_command(call: types.CallbackQuery):
    print(users)
    if call.data and call.data.startswith("button_"):
        if call.data in kb.days.keys():
            await call.answer(call.data, reply_markup=kb.class_number_kb)
        elif call.data in kb.letters:
            users[call.from_user.id][0] += call.data
            print(users[call.from_user.id])
            await bot.send_message(class_cur(call.from_user.id), reply_markup=kb.back_kb)
        elif int(call.data) in range(5,12):
            users[call.from_user.id][0] = call.data
            print(users[call.from_user.id])
            await call.answer('Расписание', reply_markup=kb.classes_kb)


def class_cur(user_id):
    class_num = users[user_id][0]
    return f'Вот тебе расписание {users[user_id][0]}'



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

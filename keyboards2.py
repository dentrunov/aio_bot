from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

d = ['Пн','Вт','Ср','Чт','Пт']
days = {d[i]: i  for i in range((len(d)))}
letters = ['А', 'Б', 'В', 'Г']
classes = dict(zip([str(j)+letter for j in range(5,12) for letter in letters], range(28)))

button_main = KeyboardButton('Главное меню', callback_data='button_main')

button_cur = KeyboardButton('Полное расписание', callback_data='button_cur')
button_cur_now = KeyboardButton('Расписание сейчас', callback_data='button_cur_now')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_cur, button_cur_now)

day_buttons = [KeyboardButton(day, callback_data='button_'+day) for day in days.keys()]
full_cur_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(*day_buttons, button_main)

class_number_buttons = [KeyboardButton(i, callback_data='button_'+str(i)) for i in range(5,12)]
class_number_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, row_width=4).add(*class_number_buttons, button_main)

class_buttons = [KeyboardButton(cl, callback_data='button_'+cl) for cl in letters]
classes_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, row_width=4).add(*class_buttons, button_main)

back_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_main)
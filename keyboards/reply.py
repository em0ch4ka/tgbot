from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard =  ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="понедельник"), KeyboardButton(text="вторник")],
        [KeyboardButton(text= "среда"), KeyboardButton(text="четверг")],
        [KeyboardButton(text="пятница"), KeyboardButton(text="суббота")],
        [KeyboardButton(text="воскресенье")],

    ],

    resize_keyboard=True
)
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main_keyboard =  ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="понедельник"), KeyboardButton(text="вторник")],
        [KeyboardButton(text= "среда"), KeyboardButton(text="четверг")],
        [KeyboardButton(text="пятница"), KeyboardButton(text="суббота")],
        [KeyboardButton(text="воскресенье")],

    ],

    resize_keyboard=True
)

inline_help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расскажи о себе", callback_data="about_info")],
        [InlineKeyboardButton(text="Кто твой создатель", callback_data="creator_info")]
    ]
)

inline_teacher_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Тау А.Ф.", callback_data="prof_tau"),
            InlineKeyboardButton(text="Кисина М.К.", callback_data="prof_kisina"),
        ],
        [
            InlineKeyboardButton(text="Ашенбренер Ю.В.", callback_data="prof_ashenbrener"),
            InlineKeyboardButton(text="Смагулова А.С.", callback_data="prof_smagulova"),
        ],
        [
            InlineKeyboardButton(text="Мусаева Ж.Т.", callback_data="prof_musaeva"),
            InlineKeyboardButton(text="Макашев Б.К.", callback_data="prof_makashev"),
        ],
        [
            InlineKeyboardButton(text="Нұртай М.Д.", callback_data="prof_nurtay"),
            InlineKeyboardButton(text="Омаров Ш.Ә.", callback_data="prof_omarov"),
        ],
        [
            InlineKeyboardButton(text="Рахатов Т.Д.", callback_data="prof_rakhatov"),
        ]
    
    ]
)
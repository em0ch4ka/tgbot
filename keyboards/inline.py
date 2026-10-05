from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расскажи о себе", callback_data="about_info")],
        [InlineKeyboardButton(text="Кто твой создатель", callback_data="creator_info")]
    ]
)

def get_teachers_keyboard():

    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="Абилдаева Г.Б.", callback_data="prof_abildaeva"))
    builder.add(InlineKeyboardButton(text="Жәнібек М.А.", callback_data="prof_ashenbrener"))
    builder.add(InlineKeyboardButton(text="Кисина М.К.", callback_data="prof_kisina"))
    builder.add(InlineKeyboardButton(text="Макашев Б.К.", callback_data="prof_makashev"))
    builder.add(InlineKeyboardButton(text="Мусаева Ж.Т.", callback_data="prof_musaeva"))
    builder.add(InlineKeyboardButton(text="Нұртай М.Д.", callback_data="prof_nurtay"))
    builder.add(InlineKeyboardButton(text="Сүлеймен А. Е", callback_data="prof_omarov"))
    builder.add(InlineKeyboardButton(text="Рахатов Т.Д.", callback_data="prof_rakhatov"))
    builder.add(InlineKeyboardButton(text="Сайманова З.Б.", callback_data="prof_saimanova"))
    builder.add(InlineKeyboardButton(text="Смагулова А.С.", callback_data="prof_smagulova"))
    builder.add(InlineKeyboardButton(text="Тау А.Ғ.", callback_data="prof_tau"))

    builder.adjust(2)
    return builder.as_markup()
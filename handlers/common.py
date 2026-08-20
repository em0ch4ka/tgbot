from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from keyboards import main_keyboard, inline_help_kb
from data import info_buttons



common_router = Router()


@common_router.message(CommandStart())

async def cmd_message(message: types.Message):

    await message.answer("Сап братанчик я бот расписание Выбери день на кнопках ниже 👇", reply_markup=main_keyboard)


@common_router.message(Command("help"))

async def cmd_help(message: types.Message):
    await message.answer("Чем могу быть полезен?", reply_markup=inline_help_kb)

@common_router.callback_query(F.data.in_(info_buttons.keys()))
async def handl_info_callback(callback: types.CallbackQuery):
    await callback.answer()

    response_text = info_buttons[callback.data]
    await callback.message.edit_text(response_text)

@common_router.message()
async def just_txt(message: types.Message):
    await message.answer("Я тебя не понял, бро. Напиши /start, /help, /teachers 🤖")
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import os
from dotenv import load_dotenv
from aiohttp import web

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
  exit("Ошибка: Токен не найден в файле .env!")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



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

inline_help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расскажи о себе", callback_data="about_info")],
        [InlineKeyboardButton(text="Кто твой создатель", callback_data="creator_info")]
    ]
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

@dp.message(CommandStart())

async def cmd_message(message: types.Message):

    await message.answer("Сап братанчик я бот расписание Выбери день на кнопках ниже 👇", reply_markup=main_keyboard)


@dp.message(Command("help"))

async def cmd_help(message: types.Message):
    await message.answer("Чем могу быть полезен?", reply_markup=inline_help_kb)


TEACHERS_INFO = {
    "prof_tau": """👨‍🏫 Тау А.Ф.
📚 Объектно-ориентированное программирование (Лекция)
📍 Главный корпус, 404""",

    "prof_kisina": """👩‍🏫 Кисина М.К.
📚 Web-программирование (Лаб)
📍 Главный корпус, 300з""",

    "prof_ashenbrener": """👨‍🏫 Ашенбренер Ю.В.
📚 Структуры данных и алгоритмы их обработки (Лаб)
📍 Главный корпус, 300е""",

    "prof_smagulova": """👩‍🏫 Смагулова А.С.
📚 Структуры данных и алгоритмы их обработки (Лекция)
📍 Главный корпус, 405""",

    "prof_musaeva": """👩‍🏫 Мусаева Ж.Т.
📚 Основы права, Основы антикоррупционной культуры (Лекция)
📍 Главный корпус, 352""",

    "prof_makashev": """👨‍🏫 Макашев Б.К.
📚 Охрана труда (Лекция)
📍 Корпус №2, 311""",

    "prof_nurtay": """👨‍🏫 Нұртай М.Д.
📚 Объектно-ориентированное программирование (Лаб)
📍 Главный корпус, 300е""",

    "prof_omarov": """👨‍🏫 Омаров Ш.Ә.
📚 Верификация, стандартизация и сертификация ПО (Лаб)
📍 Главный корпус, 300з""",

    "prof_rakhatov": """👨‍🏫 Рахатов Т.Д.
📚 Охрана труда (Лаб)
📍 Корпус №2, 517""",
}
    

@dp.message(Command("teachers"))

async def cmd_teachers(message: types.Message):
    await message.answer("Выбери преподавателя:", reply_markup=inline_teacher_kb)


@dp.callback_query(F.data.in_(TEACHERS_INFO.keys()))

async def teacher_answer(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.edit_text(TEACHERS_INFO[callback.data])

info_buttons = {
    "about_info": "Я простой бот для расписания",
    "creator_info": "Мой создатель em9"
}


@dp.callback_query(F.data.in_(info_buttons.keys()))
async def handl_info_callback(callback: types.CallbackQuery):
    await callback.answer()

    response_text = info_buttons[callback.data]
    await callback.message.edit_text(response_text)


SCHEDULE = {"понедельник": """📅 ПОНЕДЕЛЬНИК

🔹 2 пара (10:55 - 12:40)
📚 Объектно-ориентированное программирование (Лекция)
👨‍🏫 Тау А.Ф.
📍 Главный корпус, 404

🔹 3 пара (13:10 - 14:55)
📚 Структуры данных и алгоритмы их обработки (Лаб)
👨‍🏫 Ашенбренер Ю.В.
📍 Главный корпус, 300е""",
    "вторник": """📅 ВТОРНИК

🔹 2 пара (10:55 - 12:40)
📚 Web-программирование (Лаб)
👨‍🏫 Кисина М.К.
📍 Главный корпус, 300з

🔹 3 пара (13:10 - 14:55)
📚 Структуры данных и алгоритмы их обработки (Лекция)
👨‍🏫 Смагулова А.С.
📍 Главный корпус, 405""",
    "среда": """📅 СРЕДА

🔹 1 пара (09:00 - 10:45)
📚 Основы права, Основы антикоррупционной культуры (Лекция)
👨‍🏫 Мусаева Ж.Т.
📍 Главный корпус, 352

🔹 2 пара (10:55 - 12:40)
📚 Охрана труда (Лекция)
👨‍🏫 Макашев Б.К.
📍 Корпус №2, 311""",
    "четверг": """📅 ЧЕТВЕРГ

🔹 1 пара (09:00 - 10:45)
📚 Объектно-ориентированное программирование (Лаб)
👨‍🏫 Нұртай М.Д.
📍 Главный корпус, 300е

🔹 2 пара (10:55 - 12:40)
📚 Верификация, стандартизация и сертификация ПО (Лаб)
👨‍🏫 Омаров Ш.Ә.
📍 Главный корпус, 300з

🔹 3 пара (13:10 - 14:55)
📚 Охрана труда (Лаб)
👨‍🏫 Рахатов Т.Д.
📍 Корпус №2, 517""",
    "пятница": """📅 ПЯТНИЦА

🎉 Пар нет / Выходной""",
    "суббота": """📅 СУББОТА

🎉 Пар нет / Выходной""",
    "воскресенье": """📅 ВОСКРЕСЕНЬЕ

🎉 Пар нет / Выходной""",
}


@dp.message(F.text.lower().in_(SCHEDULE.keys()))
async def daily_rasp(msg: types.Message):
    day = msg.text.lower()
    await msg.answer(SCHEDULE[day])
    
        
@dp.message() 

async def just_text(msg: types.Message):
    text = msg.text.lower()
    await msg.answer("Я тебя не понял, бро. Напиши /start!, /help, /teachers 🤖")


async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_website():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():

    print("Бот стартует проврека сообщение")
    await start_website()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
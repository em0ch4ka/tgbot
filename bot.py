from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
  exit("Ошибка: Токен не найден в файле .env!")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

help_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="расскажи о себе")], [KeyboardButton(text="кто тебя создал")]
        
    ],
    resize_keyboard=True
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
    await message.answer("Чем могу быть полезен?", reply_markup=help_keyboard)
    


info_buttons = ["кто тебя создал","расскажи о себе"]


@dp.message(F.text.lower().in_(info_buttons))
async def info_bots(msg: types.Message):
    text = msg.text.lower()
    if text == "расскажи о себе":
        await msg.answer("Я простой бот для расписание")
    elif text == "кто тебя создал":
        await msg.answer("мой создатель em9")



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
    await msg.answer("Я тебя не понял, бро. Напиши /start! 🤖")

async def main():

    print("Бот стартует проврека сообщение")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
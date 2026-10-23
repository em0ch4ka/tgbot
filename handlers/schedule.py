from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.inline import get_teachers_keyboard
from datetime import datetime
from database.models import get_schedule_by_day, get_teachers


schedule_rout = Router()

db_pool = None

def set_schedule_pool(pool):
    global db_pool
    db_pool = pool



def week_day():
    week_num = datetime.now().isocalendar().week
    if week_num % 2 == 0:
        return "числитель"
    else:
        return "знаменатель"


@schedule_rout.callback_query(F.data.startswith("prof_"))
async def teacher_answer(callback: types.CallbackQuery):
    teacher_key = callback.data.replace("prof_", "", 1)

    teacher = await get_teachers(db_pool, teacher_key)

    if not teacher:
        await callback.answer("Преподаватель не найден!")
        return

    await callback.answer()
    await callback.message.answer_photo(
        photo=teacher["photo"],
        caption=teacher["bio"]
    )


@schedule_rout.message(F.text.lower().in_(["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]))
async def daily_rasp(msg: types.Message):
    day_query = msg.text.lower()
    day_display = msg.text.lower().capitalize()
    week_type = week_day()

    row = await get_schedule_by_day(db_pool, day_query, week_type)

    if not row or not row["text"]:
        await msg.answer(f"На {day_display} ({week_type}) пар не найдено или выходной!")
        return

    await msg.answer(row["text"])
    


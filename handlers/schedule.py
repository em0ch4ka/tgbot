from aiogram import Router, F, types
from aiogram.filters import CommandStart
from datetime import datetime
from database.schedule_get import get_schedule
from keyboards.reply import main_keyboard


schedule_rout = Router()
def week_day():
    week_num = datetime.now().isocalendar().week
    if week_num % 2 == 0:
        return "числитель"
    else:
        return "знаменатель"



@schedule_rout.message(CommandStart())

async def cmd_message(message: types.Message):

    await message.answer("я бот расписание выбери день на кнопках ниже 👇", reply_markup=main_keyboard)

@schedule_rout.message(F.text.lower().in_(["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]))
async def daily_rasp(msg: types.Message):
    day_query = msg.text.lower()
    day_display = msg.text.lower().capitalize()
    week_type = week_day()

    lessons = await get_schedule(day_query, week_type)

    if not lessons:
        await msg.answer(f"На {day_display} ({week_type}) пар не найдено или выходной!")    
        return

    text = f"📅 <b>Расписание на {day_display} ({week_type}):</b>\n\n"

    for lesson in lessons:
        text += (
            f"🔹 <b>{lesson.lesson_number} пара:</b> {lesson.subject.name}\n"
            f"   🕰️ <i>Время</i> {lesson.lesson_time}\n\n"
            f"   📌 <i>Тип:</i> {lesson.lesson_type}\n"
            f"   👨‍🏫 <i>Преподаватель:</i> {lesson.teacher.full_name}\n"
            f"   📍 <i>Аудитория:</i> {lesson.room}\n\n"
            
        )

    await msg.answer(text, parse_mode="HTML")


@schedule_rout.message()

async def txt_msg(msg: types.Message):
    await msg.answer("Привет я бот расписание напиши /start")



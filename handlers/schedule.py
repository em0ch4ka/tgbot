from aiogram import Router, F, types
from aiogram.filters import Command

from keyboards import inline_teacher_kb
from data import SCHEDULE, TEACHERS_INFO
from datetime import datetime


schedule_rout = Router()



def week_day():
    week_num = datetime.now().isocalendar().week()
    if week_num % 2 == 0:
        return "числитель"
    else:
        return "знаменатель"

@schedule_rout.message(Command("teachers"))
async def cmd_teachers(message: types.Message):
    await message.answer("Выбери преподавателя:", reply_markup=inline_teacher_kb)


@schedule_rout.callback_query(F.data.in_(TEACHERS_INFO.keys()))
async def teacher_answer(callback: types.CallbackQuery):

    await callback.answer()

    await callback.message.edit_text(TEACHERS_INFO[callback.data])


@schedule_rout.message(F.text.lower().in_(SCHEDULE["числитель"].keys()))
async def daily_rasp(msg: types.Message):
    day = msg.text.lower()
    week_type = week_day()
    text = SCHEDULE[week_type][day]
    await msg.answer(SCHEDULE[text])

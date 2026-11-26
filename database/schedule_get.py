from database.db import async_session_maker
from database.models import Schedulebase
from sqlalchemy.orm import selectinload
from sqlalchemy import select
import asyncio
async def get_schedule(day, week):

    async with async_session_maker() as session:

        query = select(Schedulebase).where(
        Schedulebase.day_of_week==day,
        Schedulebase.week_type == week
        ).options(selectinload(Schedulebase.teacher),
        selectinload(Schedulebase.subject)
        ).order_by(Schedulebase.lesson_number)

        result = await session.execute(query)

        return result.scalars().all()


if __name__ == "__main__":
    pairs = asyncio.run(get_schedule("понедельник", "знаменатель"))
    for par in pairs:
        print(par.lesson_number, par.subject.name, par.teacher.full_name, par.room)
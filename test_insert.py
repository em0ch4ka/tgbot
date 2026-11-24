from database.db import async_session_maker
from database.models import Schedulebase, Subjectbase
import asyncio

async def test_insert():

    async with async_session_maker() as session:

        subjectnew = Subjectbase(name="Английский язык")

        session.add(subjectnew)

        await session.flush()

        schedule = Schedulebase(
            lesson_number=3,
            lesson_type="Лекция",
            day_of_week="Среда",
            room="205 1 Корпус",
            week_type="Знаменатель",
            lesson_time="13:10-14:55",
            subject_id=subjectnew.id,
            teacher_id=6   
            )

        session.add(schedule)

        await session.commit()
        

if __name__ == "__main__":
    asyncio.run(test_insert())
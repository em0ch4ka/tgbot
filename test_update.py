from database.models import Schedulebase
from database.db import async_session_maker
import asyncio
from sqlalchemy import update

async def update_subject():
    async with async_session_maker() as session:
        query = update(Schedulebase).where(Schedulebase.week_type == "Понедельник").values(week_type="Знаменатель")
        await session.execute(query)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(update_subject())


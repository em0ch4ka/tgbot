from database.models import Subjectbase
from database.db import async_session_maker
import asyncio
from sqlalchemy import delete

async def delete_subject():
    async with async_session_maker() as session:
        query = delete(Subjectbase).where(Subjectbase.name == "Основы права, Основы антикоррупционной культуры")
        await session.execute(query)
        await session.commit()


if __name__ == "__main__":

    asyncio.run(delete_subject())
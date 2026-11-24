from database.models import Schedulebase
from database.db import async_session_maker
import asyncio
from sqlalchemy import select
from sqlalchemy.orm import selectinload


async def show_subject():

    async with async_session_maker() as session:
            query = select(Schedulebase).options(selectinload(Schedulebase.teacher), selectinload(Schedulebase.subject))
    
            result = await session.execute(query)
    
            schedule = result.scalars().all()
    
            for i in schedule:
                print(i.lesson_number, i.lesson_type, i.lesson_time, i.day_of_week, i.room, i.week_type, i.subject.name, i.teacher.full_name)
            
    


if __name__ == "__main__":
        asyncio.run(show_subject())
            

        

        
        
        
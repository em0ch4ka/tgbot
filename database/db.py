import os
import asyncpg
from dotenv import load_dotenv
from data import TEACHERS_INFO, SCHEDULE
from database.models import add_schedule, add_teachers

load_dotenv()

async def create_db_pool():
    return await asyncpg.create_pool(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 5432))
    )


async def populate_db(pool):
    for t_key, info in TEACHERS_INFO.items():
        await add_teachers(
            pool,
            teacher_key=t_key,
            bio=info.get("bio", ""),
            photo=info.get("photo", "")
        )
    print("Преподаватели успешно загружены в базу!")

    for week_type, days_dict in SCHEDULE.items():
        for day_of_week, schedule_text in days_dict.items():
                await add_schedule(
                     pool,
                     week_type=week_type,
                     day_of_week=day_of_week,
                     text=schedule_text
                    
                )
    print("Расписание успешно загружено в базу!")




async def init_db(pool):
    from database.models import create_table_schedule, create_table_teachers
    await create_table_teachers(pool)
    await create_table_schedule(pool)

    await populate_db(pool)
import asyncpg

async def add_lesson(pool,day_of_week,lesson_number,subject,lesson_type,teacher,room,week_type):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO schedule (day_of_week, lesson_number, subject, lesson_type, teacher, room, week_type)
            VALUES ($1, $2, $3, $4, $5, $6, $7);
        """, day_of_week, lesson_number,subject,lesson_type,teacher,room,week_type)


async def get_schedule_by_day(pool, day_of_week, week_type):

    async with pool.acquire() as conn:
        rows = await conn.fetch("""
        SELECT lesson_number, subject, lesson_type, teacher, room 
            FROM schedule 
            WHERE day_of_week = $1 AND (week_type = $2 OR week_type = 'all')
            ORDER BY lesson_number ASC;
        """, day_of_week, week_type)

    return rows 

# rows Чтобы поймать результат от базы данных.
async def create_table_teachers(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        teacher_key TEXT UNIQUE,
        bio TEXT,
        photo TEXT
        );
        """)


async def create_table_schedule(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            id SERIAL PRIMARY KEY,
            week_type TEXT,
            day_of_week TEXT,
            text TEXT
        )
        """)



async def add_teachers(pool, teacher_key, bio, photo):
    async with pool.acquire() as conn:
        await conn.execute("""
    INSERT INTO teachers (teacher_key, bio, photo)
            VALUES ($1, $2, $3)
            ON CONFLICT (teacher_key) DO NOTHING
        """, teacher_key, bio, photo
        )



async def add_schedule(pool, week_type, day_of_week, text):
    async with pool.acquire() as conn:
        return await conn.execute("""
        INSERT INTO schedule (week_type, day_of_week, text)
            VALUES ($1, $2, $3)
            ON CONFLICT DO NOTHING
            """,week_type, day_of_week, text)



async def get_teachers_list(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT teacherk_key FROM teachers")


async def get_teachers(pool, teacher_key):
    async with pool.acquitre() as conn:
        return await conn.fetchrow("SELECT bio, photo FROM teachers WHERE teacher_key = $1", teacher_key)

async def get_schedule_by_day(pool, day_of_week, week_type):
    async with pool.acquire() as conn:
        return await conn.fetchrow("""
            SELECT text FROM schedule 
            WHERE day_of_week = $1 AND week_type = $2
        """, day_of_week, week_type)
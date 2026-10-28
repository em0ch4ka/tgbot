import os
import asyncpg
from dotenv import load_dotenv


load_dotenv()

async def create_db_pool():
    return await asyncpg.create_pool(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 5432))
    )


async def init_db(pool):
    async with pool.acquire() as conn:

        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id BIGINT PRIMARY KEY,
                full_name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
                id SERIAL PRIMARY KEY,
                day_of_week VARCHAR(20) NOT NULL,
                lesson_number INT NOT NULL,
                subject VARCHAR(255) NOT NULL,
                lesson_type VARCHAR(50) NOT NULL,
                teacher VARCHAR(255),
                room VARCHAR(50),
                week_type VARCHAR(20) DEFAULT 'all'
            );
        """)

    
    
# Sql запросы

import asyncpg
import asyncio

async def create_table_teachers(pool):
    async with pool.acquire() as conn:
        await conn.execute("""CREATE TABLE IF NOT EXISTS teachers (
            id SERIAL PRIMARY KEY,
            teacher_key VARCHAR(50) NOT NULL,
            bio TEXT NOT NULL,
            photo VARCHAR(255)
        );
        """)



async def add_teachers(pool, teacher_key, bio, photo):
    async with pool.acquire() as connection:
        await connection.execute(""" INSERT INTO teachers (teacher_key, bio, photo)
        VALUES ($1, $2, $3) ON CONFLICT (teacher_key) DO NOTHING
        """, teacher_key, bio, photo)


async def create_table_schedule(pool,):
    async with pool.acquire() as connection:
        await connection.execute("""CREATE TABLE IF NOT EXISTS schedule (
                id SERIAL PRIMARY KEY,
                day_of_week VARCHAR(20) NOT NULL,
                week_type VARCHAR(20) NOT NULL,
                lesson_number INT NOT NULL,
                subject VARCHAR(100) NOT NULL,
                classroom VARCHAR(50),
                teacher_key VARCHAR(50)
            );
        """)

async def add_schdeule(pool, day_of_week, week_type, lesson_number, subject, classroom, teacher_key):
    async with pool.acquire() as connection:
        await connection.execute(""" INSERT INTO schedule(day_of_week, week_type, lesson_number, subject, classroom, teacher_key)
        VALUES ($1, $2, $3, $4, $5, $6)
        """, day_of_week, week_type, lesson_number, subject, classroom, teacher_key)
from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from database.db import engine
from handlers.schedule import schedule_rout

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
  exit("Токен не найден")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(schedule_rout)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот успешно стартовал!")
    try:
        await dp.start_polling(bot)
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
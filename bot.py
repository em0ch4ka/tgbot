from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from aiohttp import web
from handlers.schedule import schedule_rout, set_schedule_pool
from database.db import create_db_pool, init_db



load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
  exit("Ошибка: Токен не найден в файле .env!")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()




async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_website():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    db_pool = await create_db_pool()
    print("Успешное подключение к базе данных!")

    set_schedule_pool(db_pool)

    await init_db(db_pool)

    dp.include_router(schedule_rout)
    print("Таблицы успешно проверены/созданы!")

    await start_website()
    print("Веб-сервер для хостинга запущен!")

    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот успешно стартовал!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
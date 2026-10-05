from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from aiohttp import web
from handlers.schedule import schedule_rout
from handlers.common import common_router
from database.db import create_db_pool
from database.models import create_table_schedule, create_table_teachers


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
  exit("Ошибка: Токен не найден в файле .env!")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_router(schedule_rout)
dp.include_router(common_router)

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

    pool = await create_db_pool()
    print("Пул соединений с БД успешно создан!")

    await create_table_schedule(pool)
    await create_table_teachers(pool)
    print("Таблицы teachers и schedule проверены/созданы!")

    dp.workflow_data["db_pool"] = pool

    print("Бот стартует проврека сообщение")
    await start_website()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
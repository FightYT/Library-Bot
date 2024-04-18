import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.routers import register_handlers
from src.database.initialize import setup_db, close_db

from config import settings


dp = Dispatcher()
bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    await setup_db()
    await register_handlers(dp)
    await dp.start_polling(bot)


@dp.shutdown()
async def on_shutdown():
    """Завершаем работу базу данных при выключении бота."""
    await close_db()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
    asyncio.run(main())

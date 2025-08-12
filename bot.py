import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

# .env faylni yuklaymiz
load_dotenv()

# Tokenni .env dan o‘qiymiz
BOT_TOKEN = os.getenv("BOT_TOKEN")  # nomini BOT_TOKEN deb o‘zgartirdim, shunga mos .env bo‘lishi kerak

if not BOT_TOKEN:
    raise ValueError("ERROR: BOT_TOKEN .env faylda aniqlanmagan!")

# Routerlarni import qilamiz
from handlers.start import register_router as start_router
from handlers.chatgpt import chatgpt_router  # register_router emas, chatgpt_router
from handlers.help import help_router

async def main():
    # Logging sozlash
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Bot va Dispatcher yaratamiz
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Routerlarni qo‘shamiz
    dp.include_router(start_router)
    dp.include_router(chatgpt_router)
    dp.include_router(help_router)

    logging.info("Bot ishga tushmoqda...")

    try:
        # Pollingni boshlaymiz
        await dp.start_polling(bot)
    finally:
        # Bot sessiyasini tozalash
        await bot.session.close()
        logging.info("Bot to‘xtatildi.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to‘xtatildi.")

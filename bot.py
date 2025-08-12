import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from loader import TELEGRAM_TOKEN
from handlers.start import register_router as start_router
from handlers.chatgpt import register_router as chatgpt_router
from handlers.help import help_router

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)  # bot=bot argumentini OLIB TASHLADIM

    dp.include_router(start_router)
    dp.include_router(chatgpt_router)
    dp.include_router(help_router)

    print("Bot ishga tushmoqda...")

    try:
        await dp.start_polling(bot)  # start_polling ga bot ni BERDIM
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")

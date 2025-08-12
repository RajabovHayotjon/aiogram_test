from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.flags import get_flag
from aiogram.dispatcher.handler import CancelHandler, SkipHandler
from aiogram.types import FSInputFile
from typing import Callable, Any, Awaitable
import sqlite3

class AuthMiddleware(BaseMiddleware):
    def __init__(self, db_path: str = "bot.db"):
        super().__init__()
        self.db_path = db_path

    async def __call__(
        self,
        handler: Callable[[Message, dict], Awaitable[Any]],
        event: Message,
        data: dict
    ) -> Any:
        user_id = event.from_user.id

        # Foydalanuvchining ro'yxatdan o'tganligini tekshiramiz
        if not self.is_user_registered(user_id):
            await event.answer("❌ Siz ro'yxatdan o'tmagansiz. Iltimos, /start buyrug'ini yuboring.")
            raise CancelHandler()

        return await handler(event, data)

    def is_user_registered(self, user_id: int) -> bool:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return bool(result)

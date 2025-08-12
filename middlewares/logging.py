import logging
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from datetime import datetime

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = event.from_user
        user_id = user.id
        username = user.username or "NoUsername"
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        event_type = type(event).__name__
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(event, Message):
            text = event.text or "No text"
            logger.info(f"[{current_time}] MESSAGE from {user_id} ({username}, {full_name}): {text}")
        elif isinstance(event, CallbackQuery):
            data_callback = event.data or "No data"
            logger.info(f"[{current_time}] CALLBACK_QUERY from {user_id} ({username}, {full_name}): {data_callback}")
        else:
            logger.info(f"[{current_time}] EVENT {event_type} from {user_id} ({username}, {full_name})")

        return await handler(event, data)

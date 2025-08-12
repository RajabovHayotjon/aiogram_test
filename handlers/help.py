from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

help_router = Router()

@help_router.message(Command("help"))
async def help_command(message: Message):
    help_text = (
        "🤖 *Bot yordamchisi* 🤖\n\n"
        "Bu bot ChatGPT bilan ishlaydi va quyidagilarni bajaradi:\n"
        "- Tilni tanlash (o‘zbek yoki rus)\n"
        "- Ro‘yxatdan o‘tish (ism, telefon)\n"
        "- Siz yuborgan savollarga javob berish\n"
        "- Rasm yoki matn qabul qilish\n\n"
        "📌 /start - Botni ishga tushirish va til tanlash\n"
        "📌 /help - Ushbu yordamchi ma’lumot\n\n"
        "Savolingiz bo‘lsa, bemalol yozing!"
    )
    await message.answer(help_text, parse_mode="MarkdownV2")

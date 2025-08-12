import os
from dotenv import load_dotenv

# .env faylni yuklaymiz
load_dotenv()

class Config:
    # Telegram bot tokeni
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # OpenAI API kaliti
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Bazaga ulanish uchun fayl nomi yoki URL
    DATABASE_PATH = os.getenv("DATABASE_PATH", "bot.db")

    # Boshqa kerakli sozlamalar (masalan, admin user id, log fayli nomi va hokazo)
    ADMIN_ID = os.getenv("ADMIN_ID")  # agar kerak bo‘lsa

    LOG_FILE = os.getenv("LOG_FILE", "bot.log")

# Konfiguratsiyani osongina olish uchun
config = Config()

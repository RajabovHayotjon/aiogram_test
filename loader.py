import os
from dotenv import load_dotenv

# .env faylni yuklaymiz
load_dotenv()

# OpenAI API kaliti (.env faylda OPENAI_API_KEY bo‘lishi kerak)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Telegram bot tokeni (.env faylda BOT_TOKEN deb nomlangan bo‘lishi kerak)
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")

# Kalitlar mavjudligini tekshirish
if not OPENAI_API_KEY:
    raise ValueError("ERROR: OPENAI_API_KEY .env faylda aniqlanmagan!")

if not TELEGRAM_TOKEN:
    raise ValueError("ERROR: BOT_TOKEN .env faylda aniqlanmagan!")

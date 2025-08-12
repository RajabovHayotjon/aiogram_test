import os
from dotenv import load_dotenv
from openai import OpenAI

# .env faylni yuklaymiz
load_dotenv()

# OpenAI mijozini yaratamiz
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def ask_chatgpt(question: str) -> str:
    """
    Foydalanuvchi savoliga ChatGPT API orqali javob olish.

    :param question: Foydalanuvchidan olingan savol matni
    :return: ChatGPT javobi (matn ko‘rinishida)
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Agar bor bo‘lsa "gpt-4o" ni ishlating
            messages=[
                {"role": "system", "content": "Siz foydalanuvchiga yordam beruvchi Telegram botisiz."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1000,
            n=1
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Xatolik yuz berdi: {e}"

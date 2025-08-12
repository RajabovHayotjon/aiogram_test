import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_chatgpt(question: str) -> str:
    """
    Foydalanuvchi savoliga ChatGPT API orqali javob olish.

    :param question: Foydalanuvchidan olingan savol matni
    :return: ChatGPT javobi (matn ko‘rinishida)
    """
    try:
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="gpt-3.5-turbo",  # Kerak bo‘lsa "gpt-4o" ishlatilishi mumkin
                messages=[
                    {"role": "system", "content": "Siz foydalanuvchiga yordam beruvchi Telegram botisiz."},
                    {"role": "user", "content": question}
                ],
                temperature=0.7,
                max_tokens=1000,
                n=1
            )
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        error_msg = str(e)
        if "insufficient_quota" in error_msg or "429" in error_msg:
            return "⚠️ OpenAI API limitiga yetdingiz. Iltimos, hisobingizni tekshiring."
        return f"⚠️ Xatolik yuz berdi: {error_msg}"

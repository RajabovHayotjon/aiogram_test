import os
from dotenv import load_dotenv
from openai import OpenAI
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chatgpt_router = Router()

@chatgpt_router.message()
async def gpt_answer(message: Message, state: FSMContext):
    user_text = message.text
    if not user_text:
        await message.answer("❌ Iltimos, matn yuboring.")
        return

    try:
        # ChatGPT API chaqiruv
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Yoki kerak bo'lsa "gpt-4o"
            messages=[
                {"role": "system", "content": "Siz foydalanuvchiga yordam beruvchi Telegram botisiz."},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=500
        )

        answer = response.choices[0].message.content.strip()
        await message.answer(answer, parse_mode="HTML")

    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {e}", parse_mode="HTML")

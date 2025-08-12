from openai import OpenAI
from aiogram import Router, types
import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

register_router = Router()

@register_router.message()
async def gpt_answer(message: types.Message):
    user_text = message.text
    if not user_text:
        await message.answer("❌ Iltimos, matn yuboring.")
        return
    from aiogram import Router, types
    from aiogram.fsm.context import FSMContext
    from aiogram.fsm.state import State
    from aiogram.types import Message
    from states.register import RegisterForm
    from services.openai_service import ask_chatgpt

    chatgpt_router = Router()

    @chatgpt_router.message(RegisterForm.chat_mode)
    async def gpt_answer(message: Message, state: FSMContext):
        user_text = message.text
        if not user_text:
            await message.answer("❌ Iltimos, matn yuboring.")
            return

        try:
            # ChatGPT javobini olish
            answer = await ask_chatgpt(user_text)
            await message.answer(answer, parse_mode="HTML")

        except Exception as e:
            await message.answer(f"❌ Xatolik yuz berdi: {e}", parse_mode="HTML")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # yoki "gpt-4o"
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

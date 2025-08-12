import os
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton
)
from aiogram.fsm.context import FSMContext
from states.register import RegisterForm
from utils import get_word  # Tilga mos matnlar uchun funksiya
from sessions import register_customer  # Bazaga saqlash funksiyasi
from services.openai_service import ask_chatgpt  # ChatGPT chaqiruvchi funksiya

register_router = Router()

# /start komandasi - til tanlash
@register_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(RegisterForm.lang)
    await state.update_data({'telegram_id': message.from_user.id})

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 O'zbek tili"),
                KeyboardButton(text="🇷🇺 Русский язык")
            ]
        ],
        resize_keyboard=True
    )

    text = await get_word('lang')
    if not text:
        text = "Tilni tanlang:"
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")


# Til tanlash
@register_router.message(RegisterForm.lang)
async def lang_handler(message: Message, state: FSMContext) -> None:
    if message.text == "🇺🇿 O'zbek tili":
        lang = 'uz'
        await state.update_data({'lang': lang})
    elif message.text == "🇷🇺 Русский язык":
        lang = 'ru'
        await state.update_data({'lang': lang})
    else:
        await message.answer("❌ Tugmalardan birini tanlang.", parse_mode="HTML")
        return

    await state.set_state(RegisterForm.name)
    text = await get_word('name', lang)
    if not text:
        text = "Ismingizni kiriting:" if lang == 'uz' else "Введите ваше имя:"
    await message.answer(text, reply_markup=ReplyKeyboardRemove(), parse_mode="HTML")


# Ism qabul qilish
@register_router.message(RegisterForm.name)
async def name_handler(message: Message, state: FSMContext) -> None:
    await state.update_data({'name': message.text})
    data = await state.get_data()
    lang = data.get('lang', 'uz')

    await state.set_state(RegisterForm.phone)

    phone_button_text = "📱 Telefon raqamni yuborish" if lang == 'uz' else "📱 Отправить номер"
    phone_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text=phone_button_text,
                    request_contact=True
                )
            ]
        ],
        resize_keyboard=True
    )

    text = await get_word('phone', lang)
    if not text:
        text = "Telefon raqamingizni yuboring:" if lang == 'uz' else "Отправьте ваш номер телефона:"
    await message.answer(text, reply_markup=phone_keyboard, parse_mode="HTML")


# Telefon raqam qabul qilish
@register_router.message(RegisterForm.phone)
async def phone_handler(message: Message, state: FSMContext) -> None:
    phone = None
    if message.contact:
        phone = message.contact.phone_number
    elif message.text:
        phone = message.text.strip()

    if not phone:
        data = await state.get_data()
        lang = data.get('lang', 'uz')
        text = "Iltimos, telefon raqamingizni yuboring." if lang == 'uz' else "Пожалуйста, отправьте номер телефона."
        await message.answer(text)
        return

    await state.update_data({'phone': phone})

    # Ro'yxatdan o'tkazish bazaga
    await register_customer(state)

    data = await state.get_data()
    lang = data.get('lang', 'uz')

    # Suhbat rejimiga o'tish
    await state.set_state(RegisterForm.chat_mode)

    text1 = await get_word('registered', lang)
    if not text1:
        text1 = "Siz ro'yxatdan o'tdingiz." if lang == 'uz' else "Вы зарегистрированы."
    await message.answer(text1, reply_markup=ReplyKeyboardRemove(), parse_mode="HTML")

    text2 = await get_word('chat_ready', lang)
    if not text2:
        text2 = "Endi suhbatga o'tishingiz mumkin." if lang == 'uz' else "Теперь вы можете начать чат."
    await message.answer(text2, parse_mode="HTML")


# ChatGPT bilan suhbat rejimi
@register_router.message(RegisterForm.chat_mode)
async def chat_mode_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang = data.get('lang', 'uz')

    if message.text:
        answer = await ask_chatgpt(message.text)
        await message.answer(answer, parse_mode="HTML")

    elif message.photo:
        text_photo = (
            "📷 Rasm qabul qilindi. (Bu yerda rasmni qayta ishlash mumkin)"
            if lang == 'uz' else
            "📷 Фото принято. (Здесь можно обработать изображение)"
        )
        await message.answer(text_photo, parse_mode="HTML")
    else:
        text = "❌ Noto'g'ri format." if lang == 'uz' else "❌ Неверный формат."
        await message.answer(text, parse_mode="HTML")

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from states.register import RegisterForm

register_router = Router()


# Boshlang'ich - til tanlash
@register_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")]
    ], resize_keyboard=True)

    await message.answer("Iltimos, tilni tanlang / Пожалуйста, выберите язык:", reply_markup=kb)
    await state.set_state(RegisterForm.language_selection)


@register_router.message(RegisterForm.language_selection)
async def process_language(message: Message, state: FSMContext):
    text = message.text.strip().lower()
    if text in ["🇺🇿 o'zbekcha", "ozbekcha", "uzbek"]:
        await state.update_data(language="uz")
        await message.answer("Ro'yxatdan o'tishni boshlaymiz. Iltimos, ismingizni kiriting:",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[]))
        await state.set_state(RegisterForm.waiting_for_name)
    elif text in ["🇷🇺 русский", "russkiy", "rus"]:
        await state.update_data(language="ru")
        await message.answer("Начнем регистрацию. Пожалуйста, введите ваше имя:",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[]))
        await state.set_state(RegisterForm.waiting_for_name)
    else:
        await message.answer(
            "Iltimos, ro'yxatdan o'tish uchun tilni tanlang / Пожалуйста, выберите язык для регистрации:")


@register_router.message(RegisterForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language", "uz")

    name = message.text.strip()
    if not name:
        if lang == "uz":
            await message.answer("Iltimos, to'g'ri ismingizni kiriting:")
        else:
            await message.answer("Пожалуйста, введите корректное имя:")
        return

    await state.update_data(name=name)

    if lang == "uz":
        await message.answer("Telefon raqamingizni kiriting (masalan: +998901234567):")
    else:
        await message.answer("Пожалуйста, введите ваш номер телефона (например: +79891234567):")

    await state.set_state(RegisterForm.waiting_for_phone)


@register_router.message(RegisterForm.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language", "uz")
    phone = message.text.strip()

    if not (phone.startswith("+") and phone[1:].isdigit()):
        if lang == "uz":
            await message.answer("Telefon raqamingiz noto'g'ri formatda. Iltimos, +998901234567 shaklida yuboring:")
        else:
            await message.answer("Неверный формат номера телефона. Пожалуйста, введите номер в формате +79891234567:")
        return

    await state.update_data(phone=phone)

    name = data.get("name")

    # Bu yerda ma'lumotlarni bazaga saqlash funksiyasini chaqirish mumkin
    # save_user(message.from_user.id, name, phone)

    if lang == "uz":
        await message.answer(f"Ro'yxatdan muvaffaqiyatli o'tdingiz!\nIsm: {name}\nTelefon: {phone}",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[]))
    else:
        await message.answer(f"Вы успешно зарегистрировались!\nИмя: {name}\nТелефон: {phone}",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[]))

    await state.clear()

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True  # tugmalar faqat bir martalik ko'rinadi
    )
    return keyboard

def phone_request_keyboard(lang: str = "uz"):
    if lang == "uz":
        button_text = "📱 Telefon raqamni yuborish"
    else:
        button_text = "📱 Отправить номер"

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_text, request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

def cancel_keyboard(lang: str = "uz"):
    text = "Bekor qilish" if lang == "uz" else "Отмена"
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

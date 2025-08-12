from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Til tanlash uchun inline tugmalar
def language_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")
    )
    return keyboard

# Tasdiqlash uchun inline tugmalar (ha/yo'q)
def confirm_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="✅ Ha", callback_data="confirm_yes"),
        InlineKeyboardButton(text="❌ Yo'q", callback_data="confirm_no")
    )
    return keyboard

# Misol uchun, umumiy inline keyboard yaratish funksiyasi
def main_menu_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="ChatGPT bilan suhbat", callback_data="menu_chat"),
        InlineKeyboardButton(text="Yordam", callback_data="menu_help"),
        InlineKeyboardButton(text="Sozlamalar", callback_data="menu_settings")
    )
    return keyboard

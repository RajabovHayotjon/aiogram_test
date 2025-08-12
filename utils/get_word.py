# Lug'at shaklida turli so‘zlar va matnlar (uz va ru tillarda)
WORDS = {
    "lang": {
        "uz": "Tilni tanlang:",
        "ru": "Выберите язык:"
    },
    "name": {
        "uz": "Ismingizni kiriting:",
        "ru": "Введите ваше имя:"
    },
    "phone": {
        "uz": "Telefon raqamingizni yuboring:",
        "ru": "Отправьте ваш номер телефона:"
    },
    "registered": {
        "uz": "Siz ro'yxatdan o'tdingiz.",
        "ru": "Вы зарегистрированы."
    },
    "chat_ready": {
        "uz": "Endi suhbatga o'tishingiz mumkin.",
        "ru": "Теперь вы можете начать чат."
    },
    "error_invalid_choice": {
        "uz": "❌ Tugmalardan birini tanlang.",
        "ru": "❌ Выберите одну из кнопок."
    },
    # Qo‘shimcha so‘zlar yoki matnlarni shu yerga qo‘shishingiz mumkin
}


async def get_word(key: str, lang: str = "uz") -> str:
    """
    Berilgan kalit va til bo‘yicha so‘z yoki matnni qaytaradi.

    :param key: So‘z yoki matn kaliti (masalan, 'lang', 'name')
    :param lang: Til kodi ('uz' yoki 'ru'), default 'uz'
    :return: Tegishli matn, agar topilmasa bo‘sh qator qaytaradi
    """
    return WORDS.get(key, {}).get(lang, "")

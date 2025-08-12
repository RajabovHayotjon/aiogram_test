from typing import Optional

def format_user_info(name: str, phone: str, company: Optional[str] = None, lang: str = "uz") -> str:
    """
    Foydalanuvchi ma'lumotlarini chiroyli formatda qaytaradi.

    :param name: Foydalanuvchi ismi
    :param phone: Telefon raqami
    :param company: Kompaniya nomi (ixtiyoriy)
    :param lang: Til kodi ('uz' yoki 'ru')
    :return: Formatlangan matn
    """
    if lang == "ru":
        text = f"👤 Имя: {name}\n📞 Телефон: {phone}"
        if company:
            text += f"\n🏢 Компания: {company}"
    else:
        text = f"👤 Ism: {name}\n📞 Telefon: {phone}"
        if company:
            text += f"\n🏢 Kompaniya: {company}"
    return text


def format_error_message(error: str, lang: str = "uz") -> str:
    """
    Xatolik xabarini tilga mos formatlaydi.

    :param error: Xatolik matni
    :param lang: Til kodi
    :return: Formatlangan xatolik matni
    """
    if lang == "ru":
        return f"⚠️ Произошла ошибка: {error}"
    return f"⚠️ Xatolik yuz berdi: {error}"


def format_welcome_message(name: str, lang: str = "uz") -> str:
    """
    Xush kelibsiz xabarini formatlaydi.

    :param name: Foydalanuvchi ismi
    :param lang: Til kodi
    :return: Formatlangan xush kelibsiz matn
    """
    if lang == "ru":
        return f"Здравствуйте, {name}! Добро пожаловать!"
    return f"Salom, {name}! Xush kelibsiz!"


def format_chat_response(response: str) -> str:
    """
    ChatGPT javobini kerakli formatga keltiradi (agar kerak bo‘lsa).

    :param response: ChatGPT javobi
    :return: Formatlangan javob
    """
    # Hozircha oddiygina qaytarish, kerak bo‘lsa HTML yoki Markdown formatlash qo‘shish mumkin
    return response.strip()

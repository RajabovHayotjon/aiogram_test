import re

def validate_phone(phone: str) -> bool:
    """
    Telefon raqam formatini tekshiradi.
    Qabul qilinadigan format: +998901234567 (O‘zbekiston uchun misol),
    boshida + va undan keyin faqat raqamlar bo‘lishi kerak, umumiy uzunlik taxminan 12-15 belgidan iborat.

    :param phone: Telefon raqami matni
    :return: To‘g‘ri bo‘lsa True, aks holda False
    """
    pattern = r"^\+\d{9,14}$"  # + dan keyin 9 dan 14 gacha raqamlar
    return bool(re.match(pattern, phone))


def validate_name(name: str) -> bool:
    """
    Ismni tekshiradi.
    Oddiy qilib, ism faqat lotin yoki kirill harflaridan, shuningdek bo‘shliq va tirelardan iborat bo‘lishi mumkin.
    Minimal uzunlik 2 ta belgidan ko‘proq.

    :param name: Ism matni
    :return: To‘g‘ri bo‘lsa True, aks holda False
    """
    pattern = r"^[a-zA-Zа-яА-ЯёЁ\s\-]{2,}$"
    return bool(re.match(pattern, name.strip()))


def validate_company(company: str) -> bool:
    """
    Kompaniya nomini oddiy tekshiruv.
    Masalan, 2 dan 50 gacha belgidan iborat, maxsus belgilar cheklangan.

    :param company: Kompaniya nomi
    :return: To‘g‘ri bo‘lsa True, aks holda False
    """
    if not company:
        return False
    if len(company) < 2 or len(company) > 50:
        return False
    pattern = r"^[\w\s\.,\-&()]+$"
    return bool(re.match(pattern, company.strip()))

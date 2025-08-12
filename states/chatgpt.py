from aiogram.fsm.state import State, StatesGroup


class RegisterForm(StatesGroup):
    lang = State()      # Tilni tanlash (uz/ru)
    name = State()      # Foydalanuvchi ismi
    phone = State()     # Telefon raqami
    company = State()   # Kompaniya nomi yoki boshqa qo‘shimcha ma’lumot (agar kerak bo‘lsa)
    chat_mode = State() # ChatGPT bilan suhbat rejimi (ro‘yxatdan o‘tganidan keyin)

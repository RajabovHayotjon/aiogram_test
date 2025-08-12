from aiogram.fsm.state import State, StatesGroup

class RegisterForm(StatesGroup):
    lang = State()       # Til tanlash bosqichi (uz/ru)
    name = State()       # Foydalanuvchi ismini olish bosqichi
    phone = State()      # Telefon raqamni olish bosqichi
    chat_mode = State()  # Ro‘yxatdan o‘tganidan keyin suhbat rejimi bosqichi

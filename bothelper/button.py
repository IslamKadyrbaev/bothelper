from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MENU = ["Новости", "Курс валют", "Контактная информация", "FAQ"]

def create_main_keyboard():
    buttons = [[KeyboardButton(text=item)] for item in MENU]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
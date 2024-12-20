from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from button import create_main_keyboard, MENU
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        '''Здравствуйте, я бот помощник который может показать:
        • Новости
        • Курс валют
        • Контактную информацию
        • FAQ
    Что хотели бы узнать?''',
        reply_markup=create_main_keyboard()
    )


@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer(
        '''
    • Новости
    • Курс валют
    • Контактная информация
    • FAQ
    ''',
        reply_markup=create_main_keyboard()
    )

@dp.message(Command("about"))
async def start(message: types.Message):
    await message.answer(
        '''бот может рассказать о новостях, курсе валют, контактах и FAQ''',
        reply_markup=create_main_keyboard()
    )

@dp.message(F.text.in_(MENU))
async def menu_choice(message: types.Message):
    selected_option = message.text
    responses = {
        "Новости": "Сегодня: курс доллара вырос на 2%, акции падают.",
        "Курс валют": "Доллар: 85₽, Евро: 90₽.",
        "Контактная информация": "Наша почта: info@example.com. Телефон: +123456789.",
        "FAQ": "Часто задаваемые вопросы: почему колобок повесился?"
    }
    response = responses.get(selected_option, "Я не могу обработать ваш запрос")
    await message.answer(response)

async def main():
    print("Запуск бота...")
    await dp.start_polling(bot)

asyncio.run(main())


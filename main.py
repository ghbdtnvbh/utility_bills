import logging
from config import TOKEN_API
from parser_qr_code import parser
from aiogram.dispatcher import filters
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, кнопки пока не работают")

@dp.message_handler(filters.Text(contains='ST00012|',ignore_case=True))
async def write_data(message: types.Message):
    parser(message.text)
    await bot.send_message(message.chat.id, "Запись добавлена в db")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
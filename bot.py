import logging
import config  # конфиги мои config.tokenTelegramm
# /https://mastergroosha.github.io/telegram-tutorial-2/quickstart/
# https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html пеп код правила написания

from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.tokenTelegramm)
dp = Dispatcher(bot)

# Хэндлер на команду /test1


@dp.message_handler(commands="покажилог")
async def cmd_test1(message: types.Message):
    await message.reply("Показываю лог")

# Хэндлер на команду /test2


async def cmd_test2(message: types.Message):
    await message.reply("Запускаю компиляцию")

# Где-то в другом месте...
dp.register_message_handler(cmd_test2, commands="запустикомпиляцию")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
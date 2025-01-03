import logging
import asyncio
from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Initialize the Dispatcher
dp = Dispatcher()

# Define the command handler for /start and /help
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with /start and /help command
    """
    await message.reply("Hi \nI am an Echo Bot! \nPowered by aiogram")


@dp.message()
async def echo(message:types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)
# Entry point of the script
async def main():
    # Initialize the bot with the token
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    # Start the bot's event loop
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

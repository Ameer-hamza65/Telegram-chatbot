#@botforlife_bot


import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Initialize Dispatcher
dp = Dispatcher()

class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

def clear_past():
    reference.response = ""

# Clear command handler
@dp.message(Command(commands=["clear"]))
async def clear(message: Message):
    clear_past()
    await message.answer("I have cleared the past conversation and context.")

# Start command handler
@dp.message(Command(commands=["start"]))
async def welcome(message: Message):
    await message.answer("Hi\nI am a Telegram Bot!\nPowered by aiogram")

# Help command handler
@dp.message(Command(commands=["help"]))
async def helper(message: Message):
    help_command = """
    Hi there, I'm a Telegram bot:
    /start - Start the conversation
    /clear - Clear the chat
    /help - Show this help menu
    I hope this will help!
    """
    await message.answer(help_command)

# ChatGroq handler
@dp.message()
async def chatgroq(message: Message):
    print(f">>> USER: \n\t{message.text}")
    llm = ChatGroq(
        model="mixtral-8x7b-32768", api_key=GROQ_API_KEY
    )
    messages = [
        ("system", f"{reference.response}"),
        ("human", f"{message.text}"),
    ]
    response = llm.invoke(messages)
    reference.response = response.content
    
    print(f">>> AI: \n\t{reference.response}")
    await message.answer(reference.response)

# Main function
async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

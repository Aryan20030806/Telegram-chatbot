# STEP 1 : FRONTEND (SETUP FOR TELEGRAM BOT)

# code snippet from aiogram documentation 
import logging
from aiogram import Bot, Dispatcher, types, executor
import openai
from dotenv import load_dotenv
import os

# loading the .env file
load_dotenv()
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=telegram_bot_token) # connect the bot to Telegram 
dp = Dispatcher(bot) # create an agent to handle incoming messages

# setting the start and help commands
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\n Based on aiogram architecture and created by Aryan")

# echo handler ie will return the same message sent to the bot
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# starting the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# STEP 2 : BACKEND (INTEGRATE OPENAI API WITH TELEGRAM BOT)



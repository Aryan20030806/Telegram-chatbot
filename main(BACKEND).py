# STEP 2 : BACKEND (INTEGRATE OPENAI API WITH TELEGRAM BOT)

# code snippet from aiogram documentation 
import logging
from aiogram import Bot, Dispatcher, types, executor
import openai
from dotenv import load_dotenv
import os

# loading the .env file
load_dotenv()
Telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
OpenAI_api_key = os.getenv("OPENAI_API_KEY") 
openai.api_key = OpenAI_api_key 

# Configure logging
logging.basicConfig(level=logging.INFO)

# TO VERIFY IF THE OPENAI KEY IS LOADED
logging.info("OpenAI key loaded: %s", bool(OpenAI_api_key))

# FOR PREVIOUS RESPONSES LIKE CHATGPT
class Reference:
    def __init__(self) -> None:
        self.conversation = ""
Reference = Reference() # creating an object of the class ie initializing the class

# defining the model to be used
model = "gpt-3.5-turbo"

# INITIALIZE DISPATCHER AND BOT
bot= Bot(token=Telegram_bot_token) # connect the bot to Telegram
dp = Dispatcher(bot) # create an agent to handle incoming messages

# CLEAR THE CHAT ie RESET THE CONVERSATION
def reset_conversation():
    Reference.conversation = ""
    print("Conversation reset")

# SETTING THE COMMANDS ie start help etc etc
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello! I'm your AI assistant created by Aryan. How can I help you today?")

@dp.message_handler(commands=['reset'])
async def send_reset(message: types.Message): 
    reset_conversation()
    await message.reply("Conversation context has been reset.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("You can ask me anything! Just type your message and I'll respond to your queries.")
    help_text = "Here are some commands you can use:\n"
    help_text += "/start - Start the conversation\n"
    help_text += "/help - Get help information\n"
    help_text += "/reset - Reset the conversation context\n"
    await message.reply(help_text)

# CONFIGURE OPENAI API
@dp.message_handler()
async def handle_message(message: types.Message):
    print(f"---> User: {message.text}")
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text}
            ]
        ) 
        Reference.response = response.choices[0].message.content
        print(f"---> Assistant: \n{Reference.response}\n")
        await bot.send_message(chat_id=message.chat.id, text=Reference.response)
    except Exception as e:
        print(f"Error: {e}")
        await bot.send_message(chat_id=message.chat.id, text="Sorry, something went wrong. Please try again later.")

# START THE BOT
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)



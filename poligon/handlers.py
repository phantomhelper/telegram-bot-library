from main import bot, dp
from aiogram.types import Message
from config import root

async def send_to_root_startup(dp):
    await bot.send_message(chat_id=root, text="✅ up")

async def send_to_root_shutdown(dp):
    await bot.send_message(chat_id=root, text="⛔️ down")

@dp.message_handler()
async def echo(message: Message):
    text = f"ты написал {message.text}"
    await message.answer(text=text)

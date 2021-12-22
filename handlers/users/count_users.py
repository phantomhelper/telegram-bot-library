from loader import dp, db_users
from aiogram.types import Message

@dp.message_handler(commands=['users'])
async def count_user(message: Message):
    number = db_users.count()
    await message.answer(text=f"Ботом пользуются {number} пользователей 👥")

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Зарегестрироваться в боте",
            "/help - Получить это сообщение",
            "/users - Вывести количество пользователей")

    await message.answer("\n".join(text))

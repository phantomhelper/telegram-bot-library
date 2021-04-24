from aiogram.dispatcher.filters import Command, Text
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboard.default import menu

@dp.message_handler(command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите кнопку",
        reply_markup = menu)


@dp.message_handler(Text(equals=["Котлетки", "Макарошки", "Пюрешка"]))
    async def get_food(message: Message):
        await message.answer(f"Вы выбрали {message.text}. Спасибо",
            reply_markup = ReplyKeyboardRemove())

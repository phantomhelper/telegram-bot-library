from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from keyboards.inline.rating_buttons import rating

"""@dp.message_handler(Command("items"))
async def show_rating_menu(message: Message):
    await message.answer(text='test', reply_markup=rating)
"""


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="На продажу у нас есть 2 товара: 5 Яблок и 1 Груша. \n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=rating)

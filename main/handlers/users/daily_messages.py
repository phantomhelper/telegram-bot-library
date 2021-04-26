from loader import dp
from aiogram.types import Message
from aiogram.types import CallbackQuery
from loader import db_passagese, db_messages
from aiogram.dispatcher.filters import Command
from keyboards.inline.rating_buttons import rating

@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer('Вот товар:', reply_markup=rating)



@dp.callback_query_handler(text="rating:up")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    print(call.message.message_id)
    passage = db_messages.find_one({ "mid" : call.message.message_id })
    print(passage)
    db_passagese.update_one( {'id': passage['id'] }, {'$set': { 'rating': passage['rating']+1 }} )

@dp.callback_query_handler(text="rating:down")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("down copy")

@dp.callback_query_handler(text="rating:add")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("add copy")


# NOTE: сначала ищем ID рассказа в db_msg, далее добавляем туда рейтинг

import json, random
from loader import dp
from aiogram.types import Message
from aiogram.types import CallbackQuery
from loader import db_passagese, db_messages, db_users_shelf
from aiogram.dispatcher.filters import Command
from keyboards.default.menu import menu

@dp.callback_query_handler(text="rating:up")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    random_passage_id = db_messages.find_one({ "mid" : call.message.message_id })['id']
    random_passage = db_passagese.find_one({ "id" : random_passage_id })
    db_passagese.update_one( {'id': random_passage['id'] }, {'$set': { 'rating': random_passage['rating']+1 }} )
    await call.message.answer(text="Спасибо за оценку!")

@dp.callback_query_handler(text="rating:down")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    random_passage_id = db_messages.find_one({ "mid" : call.message.message_id })['id']
    random_passage = db_passagese.find_one({ "id" : random_passage_id })
    db_passagese.update_one( {'id': random_passage['id'] }, {'$set': { 'rating': random_passage['rating']-1 }} )
    await call.message.answer(text="Спасибо за оценку!")

@dp.callback_query_handler(text="rating:add")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    user_shelf = call.message.chat.id
    data = {
        "tid" : call.message.chat.id,
        "passage_id" : db_messages.find_one({ "mid" : call.message.message_id })['id']
    }
    db_users_shelf.insert_one(data)
    await call.message.answer(text="Добавлено!")

# NOTE: сначала ищем ID рассказа в db_msg, далее добавляем туда рейтинг

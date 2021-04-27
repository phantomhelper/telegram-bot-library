import json, random
from loader import dp
from aiogram.types import Message
from aiogram.types import CallbackQuery
from loader import db_passagese, db_messages
from aiogram.dispatcher.filters import Command
#from keyboards.inline.rating_buttons import rating, random_passage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def _random_passage():

    with open('config.json', 'r', encoding="utf8") as f:
        config = json.load(f)

    random_passage_id = random.randint(1,config['number'])
    random_passage = db_passagese.find_one({ "id" : random_passage_id })

    rating = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text="Читать полностью", url=random_passage['telegraph_url'])
        ],
        [
            InlineKeyboardButton(text="👎", callback_data="rating:down"),
            InlineKeyboardButton(text="❤️", callback_data="rating:add"),
            InlineKeyboardButton(text="👍", callback_data="rating:up")
        ]
    ])
    return random_passage, rating

# 👎❤️👍

@dp.message_handler(Command("radnom"))
async def show_items(message: Message):
    buff = _random_passage()
    text=f"""<i>{buff[0]['brief']}</i>"""
    message_id = await message.answer(f"<b>Вот рандомный абзац :</b>\n{text}", reply_markup=buff[1])
    data = {
    "mid" : message_id['message_id'],
    "title" : buff[0]['text'],
    "id" : buff[0]['id']
    }
    db_messages.insert_one(data)


@dp.callback_query_handler(text="rating:up")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    random_passage_id = db_messages.find_one({ "mid" : call.message.message_id })['id']
    random_passage = db_passagese.find_one({ "id" : random_passage_id })
    db_passagese.update_one( {'id': random_passage['id'] }, {'$set': { 'rating': random_passage['rating']+1 }} )




@dp.callback_query_handler(text="rating:down")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("down copy")

@dp.callback_query_handler(text="rating:add")
async def rating_up(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("add copy")

# NOTE: сначала ищем ID рассказа в db_msg, далее добавляем туда рейтинг

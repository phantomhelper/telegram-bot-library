from loader import dp
from loader import db_passagese
from keyboards.inline.genres import genres
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.callback_datas import search_by_genres_callback
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(regexp="По жанрам 🎭")
async def search_by_genres(message: Message):
    await message.answer(text="Выберите жанр:", reply_markup = genres)

@dp.callback_query_handler(text_contains="ламповое")
async def genres_callback(call : CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    data = db_passagese.find({"genre" : call.data})
    data_num = db_passagese.find({"genre" : call.data}).count()
    i = 0
    markup = InlineKeyboardMarkup(row_width=1)
    while i < data_num:
        button = InlineKeyboardButton(text=data[i]['text'], callback_data=data[i]['id'])
        markup.insert(button)
        i+=1
    await call.message.answer(f"Вот что я нашел:", reply_markup = markup)

@dp.callback_query_handler(text_contains="крипипаста")
async def genres_callback(call : CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    data = db_passagese.find({"genre" : call.data})
    data_num = db_passagese.find({"genre" : call.data}).count()
    i = 0
    markup = InlineKeyboardMarkup(row_width=1)
    while i < data_num:
        button = InlineKeyboardButton(text=data[i]['text'], callback_data=data[i]['id'])
        markup.insert(button)
        i+=1
    await call.message.answer(f"Вот что я нашел:", reply_markup = markup)

async def send_passage(call : CallbackQuery):
    await call.answer(cache_time=60)
    id = call.data
    data = db_passagese.find_one({"id" : int(id)})
    print(data)
    print(id)
    text = data['brief']
    rating = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text="Читать полностью", url=data['telegraph_url'])
        ]
    ])
    await call.message.answer(text=text, reply_markup=rating)

dp.register_callback_query_handler(send_passage)

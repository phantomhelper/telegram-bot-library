import time
import json
import string
import random
from aiogram import types
from threading import Thread
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db_users, db_passagese, db_messages, db_users_shelf
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

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

def get_random_string():
    # choose from all lowercase letter
    length = 16
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = ''.join(choice((str.upper, str.lower))(c) for c in result_str)
    return result_str

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    welcome_text = f"""Привет, {message.from_user.full_name}.\nБот в разработке..."""
    # await message.answer(f"Привет, {message.from_user.full_name}!")
    await bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup = menu)

    if db_users.find_one( {"tid": message.chat.id} ) == None:
        add_user = {
            "id" : config['users']+1,
            "tid" : message.chat.id,
            "is_bot" : message.from_user.is_bot,
            "first_name" : str(message.from_user.first_name),
            "username" : str(message.from_user.username),
            "last_name" : str(message.from_user.last_name),
            "language_code" : str(message.from_user.language_code),
            "code": get_random_string(),
            "last_passage": 0

        }
        print( '[user] ' + str(db_users.insert_one(add_user).inserted_id) )
        config['users']+=1
        with open("config.json", "w") as write_file:
            json.dump(config, write_file, indent=4)

@dp.message_handler(text="Мне повезет ⭐️")
async def user_random_passage(message: Message):
    buff = _random_passage()
    text=f"""<i>{buff[0]['brief']}</i>"""
    message_id = await message.answer(f"<b>{text}</b>", reply_markup=buff[1])
    data = {
    "mid" : message_id['message_id'],
    "title" : buff[0]['text'],
    "id" : buff[0]['id']
    }
    db_messages.insert_one(data)

@dp.message_handler(text="Полка 📚")
async def my_shelf(message: Message):
    tid = message.chat.id
    shelf = db_users_shelf.find({ "tid" : tid })
    shelf_num = shelf.count()
    shelf_menu = InlineKeyboardMarkup(row_width=1)
    i = 0
    while i < shelf_num:
        passage = db_passagese.find_one({"id" : shelf[i]['passage_id']})
        button = InlineKeyboardButton(text=passage['text'], callback_data=passage['id'])
        shelf_menu.insert(button)
        i+=1
    await message.answer(f"Вот что я нашел:", reply_markup = shelf_menu)

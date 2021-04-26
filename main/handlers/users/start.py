import json
import string
import random
from aiogram import types
from keyboards.default import menu
from loader import dp, bot, db_users
from aiogram.dispatcher.filters.builtin import CommandStart

def get_random_string():
    # choose from all lowercase letter
    length = 16
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = ''.join(choice((str.upper, str.lower))(c) for c in result_str)
    return result_str

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

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

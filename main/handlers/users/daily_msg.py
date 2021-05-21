import time
import json
import string
import random
import asyncio
from aiogram import types
from threading import Thread
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db_users, db_passagese, db_messages, db_users_shelf
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.start import _random_passage

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

time_day = '09:00'
#time_day = str(time.strftime("%H:%M", time.localtime())) # NOTE: ONLY FOR TESTS; TURN OFF
time_night = '20:00'

async def daily_messages():
    print('\n\n+\n\n')
    global time_day
    global time_night
    while True:
        buff = _random_passage()
        text=f"""<i>{buff[0]['brief']}</i>"""
        if str(time.strftime("%H:%M", time.localtime())) == time_day or str(time.strftime("%H:%M", time.localtime())) == time_night:
            i = 1
            while i <= config['users']:
                user = db_users.find_one({"id": i})
                text = f"<b>{text}</b>"
                message_id = await bot.send_message(chat_id=user['tid'], text=text, reply_markup=buff[1])
                data = {
                "mid" : message_id['message_id'],
                "title" : buff[0]['text'],
                "id" : buff[0]['id']
                }
                db_messages.insert_one(data)
                time.sleep(5)
        else:
            time.sleep(60)



"""loop = asyncio.get_event_loop()
loop.run_until_complete(daily_messages())"""

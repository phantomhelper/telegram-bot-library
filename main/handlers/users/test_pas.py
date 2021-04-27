"""import random, json
from loader import dp, bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from loader import db_users, db_passagese, db_messages
from aiogram.dispatcher.filters import Command
from keyboards.inline.rating_buttons import rating

@dp.message_handler(Command("test"))
async def test_pas(message: Message):

    url_button = InlineKeyboardButton(text="Читать полностью", url=random_passage['telegraph_url'])
    rating.insert(url_button)

    text=f"""<i>{random_passage['brief']}</i>"""

    message_id = await bot.send_message(chat_id=460994316, text=text, reply_markup=rating)

    data = {
        "mid" : message_id,
        "title" : random_passage['text'],
        "id" : random_passage_id
    }

    db_messages.insert_one(data)

# NOTE: сделать отдельный модуль для генерации рандомного параграффа,
# в rating_buttons добавить ссылку с импортом от рандом модуля


ежедневное сообщение:
- получить абзац
- сделать URL-button
- отправить сообщение
"""

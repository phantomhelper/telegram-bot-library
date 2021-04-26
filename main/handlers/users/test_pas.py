import random, json
from loader import dp, bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from loader import db_users, db_passagese, db_messages
from aiogram.dispatcher.filters import Command
from keyboards.inline.rating_buttons import rating

@dp.message_handler(Command("test"))
async def test_pas(message: Message):

    with open('config.json', 'r', encoding="utf8") as f:
        config = json.load(f)

    random_passage_id = random.randint(1,config['number'])
    random_passage = db_passagese.find_one({ "id" : random_passage_id })

    url_button = InlineKeyboardButton(text="Читать полностью", url=random_passage['telegraph_url'])
    rating.insert(url_button)

    text=f"""<b>{random_passage['brief']}</b>"""

    await bot.send_message(chat_id=460994316, text=text, reply_markup=rating)

    data = {
        "mid" : message.message_id,
        "title" : random_passage['text'],
        "id" : random_passage_id
    }

    db_messages.insert_one(data)

# NOTE: сделать отдельный модуль для генерации рандомного параграффа, в rating_buttons добавить ссылку с импортом от рандом модуля

import json
import datetime
from aiogram import types
from aiogram.types import Message
from loader import db_passagese, dp, db_users, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

admins = [460994316]

now = datetime.datetime.now()

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)
buff_id = config['number']

class broadcast_msg(StatesGroup):
    text=State()
    photo=State()

class passage(StatesGroup):
    title = State()
    brief = State()
    telegraph_url = State()
    audio_path = State()
    photo_path = State()
    genre = State()

@dp.message_handler(Command("add"), state=None)
async def add_psg(message: Message):
    if message.chat.id in admins:
        await message.answer("Заголовок:")
        await passage.first()

@dp.message_handler(state=passage.title)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text # ЗАГОЛОВОК
    await state.update_data(answer1=answer)
    await message.answer("Краткий рассказ:")
    await passage.next()

@dp.message_handler(state=passage.brief)
async def answer_q2(message: Message, state: FSMContext):
    answer = message.text # КРАТКИЙ РАССКАЗ
    await state.update_data(answer2=answer)
    await message.answer("Ссылка:")
    await passage.next()

@dp.message_handler(state=passage.telegraph_url)
async def answer_q3(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("Аудио (приоритет):")
    await passage.next()

@dp.message_handler(state=passage.audio_path)
async def answer_q4(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer4=answer)
    await message.answer("Фото:")
    await passage.next()

@dp.message_handler(state=passage.photo_path)
async def answer_q5(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer5=answer)
    await message.answer("Жанр:")
    await passage.next()


@dp.message_handler(state=passage.genre)
async def answer_q6(message: Message, state: FSMContext):
    answer6=message.text
    data = await state.get_data()
    answer1=data.get("answer1")
    answer6=message.text

    data = {
        "id" : buff_id+1,
        "text" : str(data.get("answer1")),
        "brief" : str(data.get("answer2")),
        "telegraph_url" : str(data.get("answer3")),
        "audio_path" : str(data.get("answer4")),
        "photo_path" : str(data.get("answer5")),
        "genre" : str(answer6),
        "rating" : 0
    }

    await state.finish()
    db_passagese.insert_one(data)
    with open("config.json", "w") as write_file:
        json.dump(config, write_file, indent=4)
    await message.answer(text="✅")

# - - - - - - - - - - - - - - - - - - - - - -

@dp.message_handler(Command("broadcast"), state=None)
async def add_psg(message: Message):
    if message.chat.id in admins:
        await message.answer("Текст:")
        await broadcast_msg.first()

@dp.message_handler(state=broadcast_msg.text)
async def answer_q1(message: Message, state: FSMContext):
    banswer = message.text # ЗАГОЛОВОК
    await state.update_data(banswer1=banswer)
    await message.answer("Фото:")
    await broadcast_msg.next()

@dp.message_handler(content_types=['photo'], state=broadcast_msg.photo)
async def answer_q2(message: Message, state: FSMContext):
    await message.photo[-1].download('broadcast.png')
    data = await state.get_data()
    banswer1=data.get("banswer1")
    users = db_users.find()
    number_f_users = users.count()
    i = 0
    while i < number_f_users:
        await types.ChatActions.upload_photo()
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('broadcast.png'), banswer1)
        await bot.send_media_group(chat_id=users[i]['tid'], media=media)
        print(data)
        i+=1
    await state.finish()

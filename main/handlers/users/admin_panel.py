from loader import db_passagese, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import json
import datetime

admins = [460994316]

now = datetime.datetime.now()

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)
buff_id = config['number']

class passage(StatesGroup):
    title = State()
    brief = State()
    telegraph_url = State()
    audio_path = State()
    photo_path = State()
    genre = State()

@dp.message_handler(commands=['add'], state="*")
async def add_title(message: Message, state: FSMContext):
    if message.chat.id in admins:
        await message.answer(text='Заголовок:')
        await passage.title.set()

@dp.message_handler(state=passage.title)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Краткий рассказ:')
    await passage.brief.set()

@dp.message_handler(state=passage.brief)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Ссылка:')
    await passage.telegraph_url.set()

    @dp.message_handler(state=passage.telegraph_url)
    async def add_brief(message: Message, state: FSMContext):
        await message.answer(text='Фото:')
        name = now.strftime("%d_%m_%Y__%H_%M")
        await message.photo[-1].download(f"/{name}.jpg")
        await passage.photo_path.set(f"photo/{name}.jpg")

@dp.message_handler(state=passage.photo_path)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Аудио (приоритет):')
    await passage.audio_path.set()

@dp.message_handler(state=passage.audio_path)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Жанр:')
    await passage.genre.set()
    data = {
        "id" : buff_id+1,
        "text" : str(passage.title),
        "brief" : str(passage.brief),
        "telegraph_url" : str(passage.telegraph_url),
        "audio_path" : str(passage.audio_path),
        "photo_path" : str(passage.photo_path),
        "genre" : str(passage.genre),
        "rating" : 0
    }

    db_passagese.insert_one(data)

    with open("config.json", "w") as write_file:
        json.dump(config, write_file, indent=4)

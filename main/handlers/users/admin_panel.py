import json
import datetime
from aiogram.types import Message
from loader import db_passagese, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

admins = [460994316]

now = datetime.datetime.now()

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)
buff_id = config['number']

class Test(StatesGroup):
    Q1=State()
    Q2=State()

@dp.message_handler(Command("test"), state=None)
async def enter_test(message: Message):
    await message.answer("Как вас зовут?")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Возраст:")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: Message, state: FSMContext):
    answer2=message.text
    data = await state.get_data()
    answer1=data.get("answer1")
    answer2=message.text
    await message.answer(f"+OK\n{answer1}\n{answer2}")
    await state.finish()


"""class passage(StatesGroup):
    title = State()
    brief = State()
    telegraph_url = State()
    audio_path = State()
    photo_path = State()
    genre = State()

@dp.message_handler(commands=['add'])
async def add_title(message: Message, state: FSMContext):
    if message.chat.id in admins:
        await message.answer(text='Заголовок:')
        await passage.title.set()
        async with state.proxy() as data:
            data['name'] = message.text

        await passage.next()
        print(passage.title)

@dp.message_handler(state=passage.title)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Краткий рассказ:')
    await passage.brief.set()
    print(passage.title)

@dp.message_handler(state=passage.brief)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Ссылка:')
    await passage.telegraph_url.set()

    @dp.message_handler(state=passage.telegraph_url)
    async def add_brief(message: Message, state: FSMContext):
        await message.answer(text='Фото:')
        await passage.photo_path.set()

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
    await message.answer(text="+OK")
"""

from data import config
from pymongo import MongoClient
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

client = MongoClient('localhost', 27017)

db = client['telegram-bot-library'] # NOTE: Главная база бота
db_users = db['users'] # NOTE: База по пользователям
db_passagese = db['passages'] # NOTE: База по отрывкам
db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам
db_messages = db['messages'] # NOTE: База с MID и отрывками

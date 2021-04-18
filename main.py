import time
import json
import telebot
import datetime
from pymongo import MongoClient
from telebot import *

client = MongoClient('localhost', 27017)

db = client['telegram-bot-library'] # NOTE: Главная база бота
db_users = db['users'] # NOTE: База по пользователям
db_books = db['books'] # NOTE: База по книгам
db_passagese = db['passages'] # NOTE: База по отрывкам
db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам

__bot_token__ = '1021184353:AAFQS9aISkFHb9oZ4KBD3xGzu6pxtD-eccI'
__root__ = 460994316
admins = [460994316]

time_day = '09:00' # NOTE: Утренее время для отправки отрывков
time_night = '20:00' # NOTE: Вечернее время для отправки отрывков

bot = telebot.TeleBot(__bot_token__)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

import time
import json
import random
import telebot
import datetime
from pymongo import MongoClient
from telebot import *
from threading import Thread

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

client = MongoClient('localhost', 27017)

db = client['telegram-bot-library'] # NOTE: Главная база бота
db_users = db['users'] # NOTE: База по пользователям
db_passagese = db['passages'] # NOTE: База по отрывкам
db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам

__bot_token__ = '1021184353:AAFQS9aISkFHb9oZ4KBD3xGzu6pxtD-eccI'
__root__ = 460994316
admins = [460994316]

time_day = '09:00' # NOTE: Утренее время для отправки отрывков
time_night = '20:00' # NOTE: Вечернее время для отправки отрывков

welcome_message = """Welcome!
In the process..."""

bot = telebot.TeleBot(__bot_token__)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def random_passage():
    random_passage_data = db_passagese.find_one({"id": random.randint(1, config['users'])})
    text = "Доброго времени суток!\nВремя интересного абзаца...\n\n" + str(random_passage_data['brief'])
    return text


def daily_messages():
    global time_day
    global time_night
    while True:
        if str(time.strftime("%H:%M", time.localtime())) == time_day:
            for i in range( config['users'] ):
                bot.send_message(config['users'][i], random_passage())
            time.sleep(60)

        elif str(time.strftime("%H:%M", time.localtime())) == time_night:
            for i in range( config['users'] ):
                bot.send_message(__root__, random_passage())
            time.sleep(60)

        time.sleep(5)


@bot.message_handler(commands=['start', 'restart'])
def start(message):

    if db_users.find_one( {"tid": message.chat.id} ) != None:
        add_user = {
            "id" : config['users']+1,
            "tid" : message.chat.id,
            "is_bot" : message.from_user.is_bot,
            "first_name" : str(message.from_user.first_name),
            "username" : str(message.from_user.username),
            "last_name" : str(message.from_user.last_name),
            "language_code" : str(message.from_user.language_code)

        }
        print( '[user] ' + str(db_users.insert_one(add_user).inserted_id) )
        config['users']+=1
        with open("config.json", "w") as write_file:
            json.dump(config, write_file, indent=4)

    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(regexp="test")
def test(message):
    bot.send_message(message.chat.id, 'ok')


daily_messages_start = Thread(target=daily_messages, args=(), daemon=True)
daily_messages_start.start()
bot.polling()

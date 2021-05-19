import time
import json
import random
import string
import telebot
import datetime
from telebot import *
from random import choice
from threading import Thread
from pymongo import MongoClient

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

client = MongoClient('localhost', 27017)

db = client['telegram-bot-library'] # NOTE: Главная база бота
db_users = db['users'] # NOTE: База по пользователям
db_passagese = db['passages'] # NOTE: База по отрывкам
db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам
db_messages = db['messages'] # NOTE: База с MID и отрывками

__bot_token__ = config['token']
__root__ = 460994316
admins = [460994316]

time_day = str(time.strftime("%H:%M", time.localtime())) # NOTE: Утренее время для отправки отрывков
time_night = '20:00' # NOTE: Вечернее время для отправки отрывков

menu_markup = types.ReplyKeyboardMarkup()
menu_my_shelf = 'Моя полка 📚'
menu_markup.add(menu_my_shelf)

welcome_message = """Welcome!
In the process..."""

bot = telebot.TeleBot(__bot_token__)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def get_random_string():
    # choose from all lowercase letter
    length = 16
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = ''.join(choice((str.upper, str.lower))(c) for c in result_str)
    return result_str

def random_passage():
    random_passage_data = db_passagese.find_one({"id": random.randint(1, config['number'])})
    return random_passage_data


def daily_messages():
    global time_day
    global time_night
    while True:
        if str(time.strftime("%H:%M", time.localtime())) == time_day or str(time.strftime("%H:%M", time.localtime())) == time_night:
            daily_passage = random_passage()
            j = 1
            while j <= config['users']:
                daily_passage_uid = db_users.find_one({ "id" : j })
                if daily_passage['photo_path'] != None:
                    photo = open(daily_passage['photo_path'], 'rb')
                    daily_msg = bot.send_photo(daily_passage_uid['tid'], photo, caption = daily_passage['brief'] + '\n\n' + daily_passage['telegraph_url'])
                    data = {
                        "mid" : daily_msg.message_id,
                        "title" : daily_passage['text'],
                        "id" : daily_passage['id']
                    }
                    db_messages.insert_one(data)
                    db_users.update_one( {'tid': daily_passage_uid['tid'] }, {'$set': { 'last_passage': daily_passage['id'] }} )

                    keyboard = types.InlineKeyboardMarkup()
                    key_rating_down = types.InlineKeyboardButton(text = "👎", callback_data = 'n' + str(daily_passage['id']));
                    key_add = types.InlineKeyboardButton(text = "➕", callback_data = 'a' + str(daily_passage['id']));
                    key_rating_up = types.InlineKeyboardButton(text = "👍", callback_data = 'y' + str(daily_passage['id']));
                    keyboard.add(key_rating_down, key_add, key_rating_up)
                    bot.send_message(daily_passage_uid['tid'], 'Как тебе рассказ?', reply_markup = keyboard)



                else:
                    audio = open(daily_passage['photo_path'], 'rb')
                    daily_msg = bot.send_audio(daily_passage_uid['tid'], audio, caption = daily_passage['brief'] + '\n\n' + daily_passage['telegraph_url'])
                    data = {
                        "mid" : daily_msg.message_id,
                        "title" : daily_passage['text'],
                        "id" : daily_passage['id']
                    }
                    db_messages.insert_one(data)
                    db_users.update_one( {'tid': daily_passage_uid['tid'] }, {'$set': { 'last_passage': daily_passage['id'] }} )

                    keyboard = types.InlineKeyboardMarkup()
                    key_rating_down = types.InlineKeyboardButton(text = "👎", callback_data = 'n' + str(daily_passage['id']));
                    key_add = types.InlineKeyboardButton(text = "➕", callback_data = 'a' + str(daily_passage['id']));
                    key_rating_up = types.InlineKeyboardButton(text = "👍", callback_data = 'y' + str(daily_passage['id']));
                    keyboard.add(key_rating_down, key_add, key_rating_up)
                    bot.send_message(daily_passage_uid['tid'], 'Как тебе рассказ?', reply_markup = keyboard)
                j+=1
            time.sleep(60)

@bot.message_handler(commands=['start', 'restart'])
def start(message):
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
    bot.send_message(message.chat.id, welcome_message, reply_markup = menu)



@bot.message_handler(regexp="ping")
def test(message):
    bot.send_message(message.chat.id, 'pong')



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data[0] == "y":
        id = int(call.data.split("y", maxsplit=1)[1])
        rating_up_passage = db_passagese.find_one({ "id" : id })
        db_passagese.update_one( {'id': id }, {'$set': { 'rating': rating_up_passage['rating']+1 }} )
        bot.send_message(call.from_user.id, 'Спасибо!\nБудем стараться подобрать Вам подходящие рассказы!')


    elif call.data[0] == "a":

        print(call)
    elif call.data[0] == "n":
        id = int(call.data.split("n", maxsplit=1)[1])
        rating_up_passage = db_passagese.find_one({ "id" : id })
        db_passagese.update_one( {'id': id }, {'$set': { 'rating': rating_up_passage['rating']-1 }} )
        bot.send_message(call.from_user.id, 'Спасибо!\nБудем стараться подобрать Вам подходящие рассказы!')


@bot.message_handler(regexp="k")
def test_test(message):
    print(message)


daily_messages_start = Thread(target=daily_messages, args=(), daemon=True)
daily_messages_start.start()
bot.polling()

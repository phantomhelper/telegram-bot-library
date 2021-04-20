import time
import json
import random
import string
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
db_messages = db['messages'] # NOTE: База с MID и отрывками

__bot_token__ = config['token']
__root__ = 460994316
admins = [460994316]

time_day = str(time.strftime("%H:%M", time.localtime())) # NOTE: Утренее время для отправки отрывков
time_night = '20:00' # NOTE: Вечернее время для отправки отрывков

markup_rating = types.ReplyKeyboardMarkup()
markup_rating_up = "👍"
markup_my = "Моя полка 📚"
markup_rating_down = "👎"
markup_rating.add(markup_rating_down, markup_my, markup_rating_up)

welcome_message = """Welcome!
In the process..."""

bot = telebot.TeleBot(__bot_token__)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def get_random_string():
    # choose from all lowercase letter
    length = 16
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def random_passage():
    random_passage_data = db_passagese.find_one({"id": random.randint(1, config['number'])})
    return random_passage_data


def daily_messages():
    global time_day
    global time_night
    while True:
        if str(time.strftime("%H:%M", time.localtime())) == time_day:
            for i in range( config['users'] ):
                data_daily_messages = random_passage()
                if data_daily_messages['photo_path'] != None:
                    photo = open(data_daily_messages['photo_path'], 'rb')
                    mid_p = bot.send_photo(__root__, photo, caption = data_daily_messages['brief'] + "\n\n" + str(data_daily_messages['telegraph_url']))
                    data = {
                        "mid" : mid_p.message_id,
                        "title" : data_daily_messages['text'],
                        "id" : data_daily_messages['id']
                    }
                    db_messages.insert_one(data)
                    db_users.update_one( {'tid': __root__ }, {'$set': { 'last_passage': data_daily_messages['id'] }} )

                elif data_daily_messages['audio_path'] != None:
                    audio  = open(data_daily_messages['audio_path'], 'rb')
                    mid_a = bot.send_audio(__root__, audio, caption = data_daily_messages['brief'] + "\n\n" + str(data_daily_messages['telegraph_url']))
                    data = {
                        "mid" : mid_a.message_id,
                        "title" : data_daily_messages['text'],
                        "id" : data_daily_messages['id']
                    }
                    db_messages.insert_one(data)
                    db_users.update_one( {'tid': __root__ }, {'$set': { 'last_passage': data_daily_messages['id'] }} )

                time.sleep(0.2)
            time.sleep(60)

        elif str(time.strftime("%H:%M", time.localtime())) == time_night:
            for i in range( config['users'] ):
                data_daily_messages = random_passage()
                if data_daily_messages['photo_path'] != None:
                    photo = open(data_daily_messages['photo_path'], 'rb')
                    bot.send_photo(__root__, photo, caption = data_daily_messages['brief'] + "\n\n" + str(data_daily_messages['telegraph_url']))

                elif data_daily_messages['audio_path'] != None:
                    audio  = open(data_daily_messages['audio_path'], 'rb')
                    bot.send_audio(__root__, audio, caption = data_daily_messages['brief'] + "\n\n" + str(data_daily_messages['telegraph_url']))
                time.sleep(0.2)
            time.sleep(60)

        time.sleep(5)


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
            "shelf_name": get_random_string(),
            "last_passage": 0

        }
        print( '[user] ' + str(db_users.insert_one(add_user).inserted_id) )
        config['users']+=1
        with open("config.json", "w") as write_file:
            json.dump(config, write_file, indent=4)
    bot.send_message(message.chat.id, welcome_message, reply_markup = markup_rating)



@bot.message_handler(regexp="ping")
def test(message):
    bot.send_message(message.chat.id, 'pong')


@bot.message_handler(regexp = markup_rating_up)
def rating_up(message):
    if message.reply_to_message.message_id != None:
        rating_up_id = db_messages.find_one({ "mid": message.reply_to_message.message_id }) # NOTE: Копируем Telegram ID сообщение
        buff = db_messages.find_one({ "mid": rating_up_id['mid'] }) # NOTE: переводим в buff данные об этом Telegram Message ID
        rating_up_passage_book = db_passagese.find_one({ "id": buff['id'] }) # NOTE: Передаем данные о книге с таким-то ID
        db_passagese.update_one( {'id': buff['id'] }, {'$set': { 'rating': rating_up_passage_book['rating']+1 }} )
        bot.send_message(message.chat.id, 'Спасибо!\nБудем стараться подобрать Вам подходящие рассказы!')

    """rating_up_data = db_users.find_one({ "tid": message.chat.id })
    rating_up_passage_book = db_passages.find_one({ "id": rating_up_data['last_passage'] })
    db_passages.update_one( {'id': rating_up_data['last_passage'] }, {'$set': { 'rating': rating_up_passage_book['rating']+1 }} )
    bot.send_message"""


@bot.message_handler(regexp="k")
def test_test(message):
    print(message)


daily_messages_start = Thread(target=daily_messages, args=(), daemon=True)
daily_messages_start.start()
bot.polling()

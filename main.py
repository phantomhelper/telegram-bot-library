import time
import json
import telebot
import datetime
#from pymongo import MongoClient
from telebot import *
from threading import Thread

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

#client = MongoClient('localhost', 27017)

#db = client['telegram-bot-library'] # NOTE: Главная база бота
#db_users = db['users'] # NOTE: База по пользователям
#db_passagese = db['passages'] # NOTE: База по отрывкам
#db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам

__bot_token__ = '1021184353:AAFQS9aISkFHb9oZ4KBD3xGzu6pxtD-eccI'
__root__ = 460994316
admins = [460994316]

time_day = '09:00' # NOTE: Утренее время для отправки отрывков
time_night = '20:00' # NOTE: Вечернее время для отправки отрывков

bot = telebot.TeleBot(__bot_token__)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def daily_messages() {
    global time_day
    global time_night
    if str(time.strftime("%H:%M:", time.localtime())) == time_day:
        for i in range( > number of users < ):
            bot.send_message(TELEGRAM_ID, TEXT)

    elif str(time.strftime("%H:%M:", time.localtime())) == time_night:
        for i in range( > number of users < ):
            bot.send_message(TELEGRAM_ID, TEXT)
}



@bot.message_handler(regexp="test")
def test(message):
    bot.send_message(message.chat.id, 'ok')


daily_messages_start = Thread(target=daily_messages())
daily_messages_start.start()
bot.polling()

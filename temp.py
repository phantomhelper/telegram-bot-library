import telebot
from telebot import *

token = "1021184353:AAFQS9aISkFHb9oZ4KBD3xGzu6pxtD-eccI"

bot = telebot.TeleBot(token)

keys = types.InlineKeyboardMarkup()
key_rating_down = types.InlineKeyboardButton(text = "👎", callback_data = 'no');
key_add = types.InlineKeyboardButton(text = "➕", callback_data = 'add');
key_rating_up = types.InlineKeyboardButton(text = "👍", callback_data = 'yes');
keys.add(key_rating_down, key_add, key_rating_up)

bot.send_message(460994316, '! ! ! ПРОВЕРКА ! ! !', reply_markup = keys)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(460994316, 'yes')
        print(call)
    elif call.data == "add":
        bot.send_message(460994316, 'add')
        print(call)
    elif call.data == "no":
         bot.send_message(460994316, 'no')
         print(call)

bot.polling()

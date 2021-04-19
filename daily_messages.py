import time
import telebot

time_day = '09:00' # NOTE: Утренее время для отправки отрывков
time_night = '18:55' # NOTE: Вечернее время для отправки отрывков

with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

client = MongoClient('localhost', 27017)

db_users = db['users'] # NOTE: База по пользователям
db_passagese = db['passages'] # NOTE: База по отрывкам
db_users_shelf = db['users_shelf'] # NOTE: База по личным полкам

def random_passage():
    random_passage_data = db_passagese.find_one({"id": random.randint(1, config['users'])})
    text = "Доброго времени суток!\nВремя интересного абзаца...\n\n" + str(random_passage_data['brief'])
    return text

def daily_messages():
    global time_day
    global time_night
    if str(time.strftime("%H:%M:", time.localtime())) == time_day:
        for i in range( config['users'] ):
            bot.send_message(config['users'][i], random_passage())

    elif str(time.strftime("%H:%M:", time.localtime())) == time_night:
        for i in range( config['users'] ):
            bot.send_message(__root__, random_passage())
    print(time_night)
    print('- ' + str(time.strftime("%H:%M:", time.localtime())))

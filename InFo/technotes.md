! ! ! ПЕРЕДАТЬ БОТА ! ! !

Token : 1021184353:AAFQS9aISkFHb9oZ4KBD3xGzu6pxtD-eccI
Botname : @NEETsoldier_bot
t.me/NEETsoldier_bot


client = MongoClient('localhost', 27017)

db = client['uh-ti_support']
tickets = db['tickets']
report = db['report']

bot = telebot.TeleBot(__bottesttoken)

print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


data = {
      "ui": message.chat.id,
      "mi": message.message_id,
      "first_name": str(message.from_user.first_name),
      "username": str(message.from_user.username),
      "last_name": str(message.from_user.last_name),
      "created": str(datetime.datetime.utcnow()),
      "text": str(message.text),
      "status": 0,
      "closed": 0,
      "by": None,
      "answer": None
  }
print(str(tickets.insert_one(data).inserted_id))

tickets.update_one( {'status':0}, {'$set': {'status':-1, 'by': message.chat.id}} )





бот отправляет пользователю художественный рассказ, рассказ сосотоит из трейлера(взятый из текста абзац), ссылки на телеграф, картинки, а иногда и сопровождающего аудиофайла
пользователь может добавить рассказ в папку "моя полка"


db_passages = {
  "text" : "ла-ла-ла-ла-ла-ла-ла-ла",
  "book_name" : "Тестовая Книга",
  "if_telegraph_url": true,
  "telegraph_url": "https://test.com/book.pdf",
  "if_audio_auth": true,
  "audio_auth": "D:/Audio_bot/book_la-la-la-la.mp3",
  ""
}

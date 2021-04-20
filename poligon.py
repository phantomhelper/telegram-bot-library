from pymongo import MongoClient
import json
client = MongoClient('localhost', 27017)


with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)


db = client['telegram-bot-library']
db_passagese = db['passages']
db_passages = {
  "id": config['number']+1,
  "text" : "ла-ла-ла-ла-ла-ла-ла-ла",
  "brief": "абзац",
  "passages_name" : "Тестовая Книга",
  "telegraph_url" : "https://test.com/test.pdf",
  "audio_path": "D:/Document/book/audio.mp3",
  "photo_path": None,
  "genre": "тестирование",
  "rating": 0
}

config['number']+=1

with open("config.json", "w") as write_file:
    json.dump(config, write_file, indent=4)

print(str(db_passagese.insert_one(db_passages).inserted_id))


print(db_passagese.find_one({"id":3}))

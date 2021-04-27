import json, random
from loader import db_passagese
with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

def random_passage():
    random_passage_id = random.randint(1,config['number'])
    random_passage = db_passagese.find_one({ "id" : random_passage_id })
    return random_passage_id, random_passage

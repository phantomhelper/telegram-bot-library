import json

with open('temp.json', 'r', encoding="utf8") as f:
    config = json.load(f)

with open("temp.json", "w") as write_file:
    json.dump(config, write_file, indent=4)

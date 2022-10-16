import json

with open ("json_01.json", encoding="utf-8") as partida:
    json_data = json.load(partida)

print(json_data)

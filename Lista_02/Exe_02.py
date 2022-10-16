import json

with open ("Json_01.json", encoding="utf-8") as partida:
    json_data = json.load(partida)

print(json_data["copa-do-brasil"][0]["time_mandante"]["nome_popular"])
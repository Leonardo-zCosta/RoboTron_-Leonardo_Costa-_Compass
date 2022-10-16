import json

with open ("Json_01.json", encoding="utf-8") as partida:
    json_data = json.load(partida)

nomeEstadio = json_data["copa-do-brasil"][0]["estadio"]["nome_popular"]
placar = json_data["copa-do-brasil"][0]["placar"]
status= json_data["copa-do-brasil"][0]["status"]

print(f"{nomeEstadio}\n{placar}\n{status}")

import json

arquivo = open("json1.json", encoding="utf-8")
data = json.load(arquivo)

nomeEstadio = data["copa-do-brasil"][0]["estadio"]["nome_popular"]
placar = data["copa-do-brasil"][0]["placar"]
status = data["copa-do-brasil"][0]["status"]

print(nomeEstadio)
print(placar)
print(status)


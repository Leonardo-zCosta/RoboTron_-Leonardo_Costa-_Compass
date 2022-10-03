import json

arquivo = open("json1.json", encoding="utf-8")
data = json.load(arquivo)


print(data["copa-do-brasil"][0]["time_mandante"]["nome_popular"])


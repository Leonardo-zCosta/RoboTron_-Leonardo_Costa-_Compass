import json

arquivo = open("json2.json", encoding="utf-8")
campeonato = json.load(arquivo)
print(campeonato)


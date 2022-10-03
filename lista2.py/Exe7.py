import json

arquivo = open("json2.json", encoding="utf-8")
campeonato = json.load(arquivo)

for cada in campeonato:
    print(cada)


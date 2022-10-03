import json

arquivo = open("json1.json", encoding="utf-8")
data = json.load(arquivo)
print(data)

arquivo.close()


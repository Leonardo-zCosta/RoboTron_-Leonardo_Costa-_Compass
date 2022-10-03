import json

arquivo = open("json2.json", encoding="utf-8")
campeonato = json.load(arquivo)

print(campeonato["edicao_atual"]["edicao_id"])
print(campeonato["fase_atual"]["fase_id"])
print(campeonato["rodada_atual"]["nome"])


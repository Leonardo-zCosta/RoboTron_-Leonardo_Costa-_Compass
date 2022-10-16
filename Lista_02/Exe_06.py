import json

with open('json_02.json', 'r', encoding='utf-8') as campeonato:
    json_02 = json.load(campeonato)
    
edi = json_02["edicao_atual"]
fas = json_02["fase_atual"]
rod = json_02["rodada_atual"]

lista = [edi, fas, rod]

for i in lista:
    for j in i:
        print(f"\"{j}\": \"{i[j]}\"")
        break

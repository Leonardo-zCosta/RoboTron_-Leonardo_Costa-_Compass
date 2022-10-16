import json

with open("json_02.json", encoding="utf-8") as campeonato:
    json_02 = json.load(campeonato)
    
    for chave in json_02:
        print(chave)

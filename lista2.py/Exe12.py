import pandas as pd;

arquivo = pd.read_csv("link.csv", encoding="utf-8")

atorUm = arquivo.loc[(arquivo['Year'] == 1991)]
atorDois = arquivo.loc[(arquivo['Year'] == 2016)]

print(atorUm["Name"])
print(atorDois["Name"])
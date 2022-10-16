import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

actor = arquivo.iloc[23]

print(arquivo.iloc[23])
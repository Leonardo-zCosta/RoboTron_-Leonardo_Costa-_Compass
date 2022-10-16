import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

actor = arquivo.loc[arquivo["Year"] == 1993, "Name"]

print(actor)


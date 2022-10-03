import pandas as pd;

arquivo = pd.read_csv("link.csv", encoding="utf-8")

movie = arquivo.iloc[12]

print(movie)

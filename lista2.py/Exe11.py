import pandas as pd;

arquivo = pd.read_csv("link.csv", encoding="utf-8")

movie = arquivo.loc[(arquivo['Year'] == 1993)]


print(movie["Name"])

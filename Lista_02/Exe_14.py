import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

for ano in range(1987, 2000):
    actor = arquivo.loc[arquivo["Year"] == ano]
    print(actor[["Name", "Age"]])
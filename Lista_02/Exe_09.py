import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

print(arquivo["Age"])
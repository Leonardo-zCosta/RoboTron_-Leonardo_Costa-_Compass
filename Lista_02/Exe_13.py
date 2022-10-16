import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

new = arquivo[["Movie", "Year"]]

print(new)
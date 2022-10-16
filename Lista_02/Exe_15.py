import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

Movies = arquivo.loc[arquivo["Movie"] != "The Revenant"]

print(Movies["Movie"])
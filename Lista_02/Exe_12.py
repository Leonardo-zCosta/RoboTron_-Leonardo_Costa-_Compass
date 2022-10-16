import pandas as pd

arquivo = pd.read_csv("link.csv", encoding="utf-8", sep=",")

actor_01 = arquivo.loc[arquivo["Year"]== 1991, "Name"]
actor_02 = arquivo.loc[arquivo["Year"]== 2016, "Name"]

print(f" {actor_01},\n {actor_02}")
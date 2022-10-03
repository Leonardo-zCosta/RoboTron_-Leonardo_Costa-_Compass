import pandas as pd;

arquivo = pd.read_csv("link.csv", encoding="utf-8")

for idade in range(1987, 1999):
    ator = arquivo.loc[(arquivo["Year"]) == idade ]
    print(ator[["Name", "Age"]])
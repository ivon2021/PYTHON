import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")

df["NACIONALIDAD"] = "CHILE"

print(df)

del df["NACIONALIDAD"]

print(df)
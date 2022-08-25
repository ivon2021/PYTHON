import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")

df["NACIONALIDAD"] = "CHILE"

df.to_csv("clientes_modificado.csv",sep=";",index=False)
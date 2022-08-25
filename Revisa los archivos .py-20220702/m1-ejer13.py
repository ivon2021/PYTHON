import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")

df["BONO"] = df["MONTO"]/df["PUNTAJE_CREDITICIO"]

print(df)
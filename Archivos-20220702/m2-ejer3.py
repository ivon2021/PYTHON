import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")

print(df_clientes.dtypes)

df_clientes["PUNTAJE_CREDITICIO"] = df_clientes["PUNTAJE_CREDITICIO"].astype("float64")

print(df_clientes.dtypes)
import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")

print(df_clientes.dtypes)

df_clientes = df_clientes.rename(columns={"FECHA_NAC":"FECHA_NACIMIENTO"})

print(df_clientes.dtypes)
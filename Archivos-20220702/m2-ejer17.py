import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")
df_clientes2 = pd.read_csv("clientes2.csv",encoding="latin-1", sep=";")

print(df_clientes)
print(df_clientes2)

df_clientes = df_clientes.append(df_clientes2)
print(df_clientes)
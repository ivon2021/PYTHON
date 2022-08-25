import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")

print(df_clientes)
df_clientes = df_clientes.drop(df_clientes.iloc[0:10].index)
print(df_clientes)
import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")

df_clientes = df_clientes.set_index("RUT")

print(df_clientes.iloc[5])
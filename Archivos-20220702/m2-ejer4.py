import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")


print(df_clientes.loc["21.930.631-4"])

 


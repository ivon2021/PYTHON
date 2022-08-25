import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")

df_final = df.loc[df['PUNTAJE_CREDITICIO'] <= 8.0]

print(df_final)
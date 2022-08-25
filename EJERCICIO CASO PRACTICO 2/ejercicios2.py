import pandas as pd

df_consultas = pd.read_csv("consultas.csv",sep=";")
print(df_consultas.iloc["4.367.282-7":"19.500.328-3"])

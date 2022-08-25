import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

df2 = df["Nombre"].str.split(" ",expand=True)
df2.columns=["Primer Nombre","Segundo Nombre","Primer Apellido","Segundo Apellido"]
print(df2)
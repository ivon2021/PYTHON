import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

df2 = df["Nombre"].str.split(" ",expand=True)
df2.columns=["Nombre","Segundo Nombre","Primer Apellido","Segundo Apellido"]
df = df.join(df2, rsuffix = "_df2", lsuffix="_df")
print(df.dtypes)
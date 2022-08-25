import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

df2 = df["Nombre"].str.split(" ",expand=True)

print(df2)
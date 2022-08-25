import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

print(df.loc[df["Monto"] > 5000000])
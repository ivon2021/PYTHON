import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

df2 = pd.DataFrame([["1",2],["3",4]])
df = df.join(df2)
print(df)
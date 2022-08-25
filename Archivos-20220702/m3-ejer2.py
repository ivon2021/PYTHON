
import pandas as pd
df = pd.read_csv("ejemplo.csv",encoding="latin-1",sep=";")

for index,row in df.iterrows():
	primer_nombre = row["Nombre"].split(" ")[0]
	print(primer_nombre)

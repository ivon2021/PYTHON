import pandas as pd
import numpy as np

df = pd.read_csv("ejemplo2.csv",encoding="latin-1",sep=";")

df2 = df.pivot_table(index="BANCO",values="MONTO", columns="SEXO", aggfunc={np.mean,np.min,np.max})

print(df2)
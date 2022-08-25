import pandas as pd
df_banco_A = pd.read_csv("bancoA.csv",encoding="latin-1",sep=";")
df_banco_B = pd.read_csv("bancoB_2.csv",encoding="latin-1",sep=";")

df_banco_A = df_banco_A.merge(df_banco_B,left_on="ID",right_on="RUT",suffixes={"_bancoA","_bancoB"}, how="left")

print(df_banco_A)
import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
#print(df_pacientes)

df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")

#12
df_nacionalidad = pd.read_csv("nacionalidad.csv",encoding="utf-8",sep=";")

df_pacientes = df_pacientes.merge(df_nacionalidad,left_on="RUT",right_on="RUT",how="left")
print(df_pacientes.dtypes)
print(df_pacientes.head())
print(df_pacientes)

print(df_pacientes["País_origen"])
print(df_pacientes["Ciudad_Residencia"])
print(df_pacientes.iloc[667])
print(df_pacientes.iloc[668])

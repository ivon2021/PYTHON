import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
#print(df_pacientes)

df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")

#11
df2 = df_pacientes["Nombre"].str.split(" ",expand=True)
df2.columns=["Primer Nombre","Segundo Nombre","Primero Apellido","Segundo Apellido"]
print(df2)
df_pacientes = df_pacientes.join(df2)
print(df_pacientes.shape)
print(df_pacientes.head())

import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
#print(df_pacientes)

df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")


#9
print(df_pacientes)
df_pacientes2["Nombre"] = df_pacientes2["Nombre"].str.upper()
df_pacientes = df_pacientes.append(df_pacientes2)
print(df_pacientes)

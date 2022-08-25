import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
#print(df_pacientes)

df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")
#print(df_pacientes2)

print(df_pacientes2["Fecha_Nacimiento"])
df_pacientes2["Fecha_Nacimiento"] = df_pacientes2["Fecha_Nacimiento"].str.replace("_/","/")
print(df_pacientes2["Fecha_Nacimiento"] )

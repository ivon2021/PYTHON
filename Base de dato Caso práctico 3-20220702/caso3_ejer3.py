import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")

print(df_pacientes)
df_pacientes["Nombre"] = df_pacientes["Nombre"].str.upper()
print(df_pacientes.head())




    

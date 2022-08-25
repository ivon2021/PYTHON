import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
print(df_pacientes)


df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")
#print(df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX"))])
df_pacientes2 = df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX"))
                                  & ~(df_pacientes2["Nombre"].str.contains("XXXX"))]
print(df_pacientes2)

    

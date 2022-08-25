import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="latin-1",sep=";")

print(df_pacientes)
print(df_pacientes.dtypes)
print(df_pacientes["Nombre"].str[0:10])


    

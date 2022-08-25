import pandas as pd

df_pacientes= pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")

df_pacientes["Monto_Deuda"]=df_pacientes["Monto_Deuda"]*1.03

df_pacientes.to_csv("datos_pacientes_reajustado.csv",sep=";",index=False)




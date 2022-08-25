import  pandas as pd
df_pacientes=pd.read_csv("datos_pacientes.csv",encoding="latin-1",sep=";")

print(df_pacientes)

lista_montos = []
for index,row in df_pacientes.iterrows():
    valor = row["Monto_Deuda"]
    valor = valor/ 700
    lista_montos.append(valor)
print(lista_montos[0:10])

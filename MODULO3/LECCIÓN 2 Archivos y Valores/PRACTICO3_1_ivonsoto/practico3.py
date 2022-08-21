#Problema 1:
#Escribir un programa que genere y muestre por pantalla
# un Dataframe ordenado de la  siguiente forma:

#Mes	Gastos	Ventas
#Enero	20000	30500
#Febrero18000	42300
#Marzo	25000	82000
#Abril	30000	54000
#Mayo	20000	38000
#Junio	17000	50000

#realizo data excel
import pandas as pd


ventas = {'Mes': ['Enero', 'Febrero', 'Marzo', 'abril', 'Mayo', 'Junio'],
        'Gastos': [20000, 18000, 25000, 30000, 20000, 17000],
        'Ventas': [30500, 42300, 82000, 54000, 38000, 50000]}

ventas = pd.DataFrame(ventas, columns = ['Mes', 'Gastos', 'Ventas'])
print(ventas)




"""
Problema 1:
El archivo info.csv contiene los valores ficticios de diferentes 
empresas en la bolsa con las siguientes  columnas:
	nombre (nombre de la empresa), 
	Final (precio de la acción al cierre de bolsa), 
	Máximo (precio  máximo de la acción durante la jornada), 
	Mínimo (precio mínimo de la acción durante la jornada), 
	volumen  (Volumen al cierre de bolsa), 
	Efectivo (capitalización al cierre). 
Codificar una función que construya un  DataFrame a partir del archivo csv 
y devuelva otro DataFrame con el mínimo, el máximo y la media de cada  columna.
"""

from statistics import median
import pandas as pd

#funciona
"""
data = pd.read_csv('info.csv',index_col = 0, 
                   sep=';',decimal=',',thousands='.', encoding='latin-1')
data =pd.DataFrame([data.min(), data.max(), data.mean()],
                        index=['Mínimo', 'Máximo', 'Media'])
print(data)
"""
#creeamos el data el cula nos va a traer el archivo info.csv
data = pd.read_csv('info.csv',index_col = 0, sep=';'
                   ,decimal=',',thousands='.', encoding='latin-1')

#definimos la funcion calculo 
def calculo(data):
    #declaramos el dataframe el cual retornara y
    # nos calulara el min,max,media del archivo info.csv,
    return pd.DataFrame([data.min(), data.max(),
                         data.mean()], index=['Mínimo', 'Máximo', 'Media'])
#declaramos la variable resultado para poder imprimir
resultado = calculo(data)

print(resultado)

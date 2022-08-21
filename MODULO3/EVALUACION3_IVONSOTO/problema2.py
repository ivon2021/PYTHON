"""
Problema 2:
El fichero info2.csv contiene información sobre tripulantes de un buque. 
Escribir un programa con los  siguientes requisitos:
"""
import pandas as pd

#print("**************enunciado1******************************\n")
#Crear un DataFrame con los datos del
# fichero.
data2 = pd.read_csv('info2.csv',index_col = 0, 
                   sep=';',decimal=','
                   ,thousands='.'
                   , encoding='latin-1')
print(data2)

print("**************enunciado2******************************\n")
#Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
# los nombres de sus  columnas y filas, los tipos de datos de las columnas, 
# las 10 primeras filas y las 10 últimas filas

print('Dimensiones:', data2.shape)
print('Número de elemntos:', data2.size)
print('Nombres de columnas:', data2.columns)
print('Nombres de filas:', data2.index)
print('Tipos de datos:\n', data2.dtypes)
print('Primeras 10 filas:\n', data2.head(10))
print('Últimas 10 filas:\n', data2.tail(10))

#Mostrar por pantalla los datos del pasajero con identificador 146
print("**************enunciado3******************************\n")
print(data2.loc[146])


print("**************enunciado4******************************\n")
#Mostrar por pantalla las filas pares del DataFrame

print(data2.iloc[range(0, data2.shape[0],2)])


#Mostrar por pantalla los nombres de las personas que iban en primera
# clase ordenadas alfabéticamente.  
print("**************enunciado5******************************\n")
print(data2[data2["Pclass"]==1]['Name'].sort_values())

#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print("**************enunciado6******************************\n")
print(data2['Survived'].value_counts()/data2['Survived'].count() * 100)


print("**************enunciado7******************************\n")
#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
print(data2.groupby('Pclass')['Survived'].value_counts(normalize=True))


print("**************enunciado8******************************\n")
#Eliminar del DataFrame los pasajeros con edad desconocida
data2.dropna(subset=['Age'])
print(data2)

print("**************enunciado9******************************\n")

#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(data2.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

print("**************enunciado10******************************\n")
#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
data2['Young'] = data2['Age'] < 18

print("**************enunciado11******************************\n")
#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
data2['Young'] = data2['Age'] < 18 
print( data2.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)


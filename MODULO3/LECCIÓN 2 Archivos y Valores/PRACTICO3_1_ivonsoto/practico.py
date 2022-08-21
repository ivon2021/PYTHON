#Problema 2: 
# Escribir un programa que genere y muestre por pantalla 
# dos Dataframe o matrices de 4x4 y  realice operaciones
# matemáticas ocupando las librerías que se han visto en este módulo.

import numpy as np
import pandas as pd

matriz= np.array([[11,22,33,44],
                  [66,55,77,88],
                  [99,10,13,14],
                  [17,18,21,32]])
#print(matriz)
#muestra la matriz 4x4
df=pd.DataFrame(matriz, columns=["a","b","c","d"])
print(df)

#calcula maximo y monimo de la matriz
plan=[x for y in matriz for x in y]
print(f"el valor máximo es: {max(plan)} y el mínimo es: {min(plan)}")

 #calcula el promedio  a lo largo de la fila.
print("El promedio  a lo largo de la fila es:\n",np.mean(df,axis=1))

 #calcula la suma total, promedio total y cantidad de elementos.
elementos = 0
sumatoria = 0
for fila in matriz:
    for elemento in fila:
        sumatoria += elemento
        elementos += 1

promedio = sumatoria / elementos
print(
f"La suma es: {sumatoria} y el promedio es {promedio}, para la matriz que tiene {elementos} elementos"
)

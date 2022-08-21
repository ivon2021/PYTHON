#escribir  una funcion que recib un diccionario con 
# las notas de los alumnos en curso en un examen y
#devuelva una serie con la nota minima, la maxima,
#media y la desviacion tipica.

#ejercicio pag 42 modulo3

import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos =pd.Series([notas.min(), notas.max(), notas.mean(),
                             notas.std()], index=['Min', 'Max',
                                                  'Media','Desviación típica'])
    return estadisticos
notas ={'Juan':9, 'María':6.5, 'Pedro':4,
        'Carmen':8.5, 'Luis':5}
print(estadistica_notas(notas))
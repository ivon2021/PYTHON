#ejercicio3 modulo3 pag43
#escribir una funcion que reciba un diccionario 
# con las notas de los alumnos en curso en un examen y 
# devuelva una serie con las notas de los alummnos
# aprobados ordenadas de mat¿yor a menor.

import pandas as pd

def aprobados(notas):
    notas =pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending = False)

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen':8.5, 'luis':5}
print(aprobados(notas))
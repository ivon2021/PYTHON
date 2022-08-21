#3. Suma total: crea una función que toma una lista
# y devuelve la suma de todos los  valores de la matriz.

lista=[2, -4, 3, 1,100]
def suma_total(lista):
 suma = 0
 for i in range( len(lista)):
    suma += lista[i]

 print([2, -4, 3, 1,100])
 print("La suma de la lista es:", suma)

suma_total(lista)


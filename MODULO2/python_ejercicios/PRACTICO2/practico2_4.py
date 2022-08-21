#4. Promedio: crea una función que toma una
# lista y devuelve el promedio de todos los  valores.


lista=[1,2,3,4,7]

def promedio(lista):
    suma = 0

    for i in range(len (lista)):
     suma += lista[i]
     promedio = suma / len(lista)
    return promedio
print(lista)
print("El Promedio de la lista es:", promedio(lista))


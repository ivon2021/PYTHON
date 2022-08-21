#7. Máximo: crea una función que toma una lista
# y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función 
# devuelva False.


lista = [10, 104, 8, -1, 54]

def maximo(lista):
 
 valor = 0

 for num in lista:
   if (valor == 0 or num > valor):
        valor = num

 print(lista,'Maximo valor:', valor)
maximo(lista)

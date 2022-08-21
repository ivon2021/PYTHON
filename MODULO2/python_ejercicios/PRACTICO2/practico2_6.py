#6. Mínimo: crea una función que tome una lista 
# de números y devuelva el valor mínimo  en la lista.
# Si la lista está vacía, haga que la función devuelva 
# False.



lista = []

def minimo(lista):
 
 valor = 0

 for num in lista:
   if (valor == 0 or num < valor):
        valor = num

 print(lista,'Minimo valor:', valor)
minimo(lista)



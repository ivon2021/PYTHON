#2.	Contar positivos: dada una lista de números, 
# cree una función para reemplazar el 
# último valor con el número de valores positivos.

lista=([1,6,-4,-2,-7,9,10,14])
def reemplazar(lista):
    
    contador = 0
    for i in range( len(lista)):
     if (lista[i] > 0):
        contador += 1
    lista[len(lista)-1] = contador
    

    print([1,6,-4,-2,-7,9,10,14])
    print("Los numeros positivos son:",contador)
   # return lista
reemplazar(lista)
 

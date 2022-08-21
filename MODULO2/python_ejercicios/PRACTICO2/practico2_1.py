#1.	Tamaño grande: dada una lista, escriba 
# una función que cambie todos los números
# positivos de la lista a "big".


lista=([-1, 3, 5,-5,7])
def biggie_size(lista):
     
    for i in range (len(lista)):
        if (lista[i] > 0):
            lista[i] = "grande"
          #  return lista
        
    print(lista)
biggie_size(lista)


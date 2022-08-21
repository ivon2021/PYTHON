#5. Longitud: crea una función que toma una 
# lista y devuelve la longitud de la lista.


lista = [37,2,1,-9]

def longitud(lista):
     
     con = 0
     for i in range (len (lista)):
      con += 1
   
     print(lista, "La Longitud es:",con)
longitud(lista)
#4.-Itera a través de un diccionario con valores de listas 
# Crea una función printInfo(some_dict) que, dado un diccionario
# cuyos valores son todas  listas, imprima el nombre de cada clave
# junto con el tamaño de su lista, y luego imprima los  valores 
# asociados dentro de la lista de cada clave. Por ejemplo:

#creamos el diccionario
dojo = {
 'locations': ['San Jose', 'Seattle', 'Dallas',
               'Chicago', 'Tulsa', 'DC', 'Burbank '],
 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 
                 'Graham', 'Patrick', 'Minh',  'Devon']
}


#definimos la funcion printInfo
def  printInfo ( lista ):
    #recorremos con un for el diccionario
   for clave in  lista :
       #se obtiene el largo de la lista
        print (len (lista [clave ]), clave)
        for  i  in  range(len(lista[clave])):
            print ( lista [ clave ][ i ])
        print( "" )
        
#llamamos a la funcion printInfo
printInfo(dojo)
# output:
# 7 LOCATIONS
#San Jose Seattle Dallas Chicago Tulsa DC Burbank
#INSTRUCTORS Michael Amy Eduardo Josh Graham Patrick Minh Devon

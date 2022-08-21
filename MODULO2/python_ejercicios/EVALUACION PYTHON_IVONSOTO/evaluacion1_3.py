#3. Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, 
# dada una lista de  diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave 
# para cada diccionario. Por ejemplo, 
# iterateDictionary2 ('first_name', students) debería  generar:
#Michael
#John
#Mark
#KB
#Y iterateDictionary2('last_name', students) debería generar:
#Jordan
#Rosales
#Guillen
#Tonel

#definimos nuestro listado de alumnos
alum1 = [
 {'Nombre': 'Michael', 'Apellido' : 'Jordan'},
 {'Nombre' : 'John', 'Apellido' : 'Rosales'},
 {'Nombre' : 'Mark', 'Apellido' : 'Guillen'},
 {'Nombre' : 'KB', 'Apellido' : 'Tonel'}
 ]

#muestra listado de nombres y apellidos en listas
def lista2 (valor , alum1):
    #recorremos el largo del directorio alum1 con su posicion y valor
    for i  in range(len(alum1)):
      print(alum1 [ i ][ valor  ])
   
lista2 ( 'Nombre',alum1 )     
lista2('Apellido',alum1)
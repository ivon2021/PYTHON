#2. Itera a través de una lista de diccionarios 
# Crea una función iterateDictionary(some_list) que,
# dada una lista de diccionarios, la función
# recorra cada diccionario de la lista e imprime 
# cada clave y el valor asociado. Por ejemplo,  
# dada la siguiente lista:

print ( "******************************************************" )
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ]

def iterateDictionary(students):
    for i in range(len(students )):
        print( "first_name- " + students [ i ][ 'first_name' ] 
               + ", last_name - " + students [ i ][ 'last_name' ])
       
iterateDictionary(students)
  
# La salida debería ser: (Está bien si cada 
# clave y valor quedan en dos líneas separ adas)

# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

"""
EVALUACION FINAL MODULO2
4. Itera a través de un diccionario con valores de listas
Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores 
son todas  listas, imprima el nombre de cada clave junto con el tamaño de su lista, 
y luego imprima los  valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
 'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank '],
 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh',  'Devon']

}

printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

dojo = {'location':['San jose', 'Seatle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors':['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for clave,valor in dojo.items():
        print(clave, '->',len(valor))
        for value in valor:
            print(value)
            
        printInfo(dojo)
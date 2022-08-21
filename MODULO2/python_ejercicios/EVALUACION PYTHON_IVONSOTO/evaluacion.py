#1. Actualiza los valores en diccionarios y listas

x  = [ [ 5 , 2 , 3 ], [ 10 , 8 , 9 ] ]
estudiantes  = [
     { 'nombre' :   'Miguel' , 'apellido' : 'Jordan' },
     { 'nombre' : 'Juan' , 'apellido' : 'Rosales' }
]
deportes  = {
    'baloncesto' : [ 'Kobe' , 'Jordan' , 'James' , 'Curry' ],
    'fútbol' : [ 'Messi' , 'Ronaldo' , 'Rooney' ]
}
z  = [ { 'x' : 10 , 'y' : 20 } ]

#responder
#1. Cambia el valor 10 en x a 15. Una vez que haya
# terminado, x ahora debería ser  [[5,2,3], [15,8,9]].
x [ 1 ][ 0 ] = 15
print ( x )

   
#2. Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
    
estudiantes [ 0 ][ 'apellido' ] =  "Bryant"
print ( estudiantes )

 #3. En el directorio sports_directory, cambia 'Messi' a 'Andres'
deportes [ 'fútbol' ][ 0 ] =  'Andrés'
print( deportes )

#4. Camba el valor 20 en z a 30
z [ 0 ][ 'y' ] = 30
print ( z )








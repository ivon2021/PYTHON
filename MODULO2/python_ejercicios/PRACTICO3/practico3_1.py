#1.	Codificar un programa que pida al u
# suario una palabra y luego muestre por pantalla  
# una a una las letras de la palabra introducida 
# empezando por la última.

palabra=input("Introduce una palabra:" )
for i in range(len(palabra)-1, -1, -1 ):
    print(palabra[i],i)
    
    
#palabra=str(input("Introdusca una palabra: \n " ))
#contador=len(palabra)-1 # cuenta la palabra introducida
#while contador>=0: # mientras la palabra introducida sea mayor a 0 entra al bucle
#print(palabra[contador])
#contador=contador -1
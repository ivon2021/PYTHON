#3. Sumatoria: crea una función que acepta una 
# lista y devuelve la suma de los números  de la lista

def sumatoria(lista):
    
    suma=0
    
    for numeros in lista:
            suma +=numeros
            
    return suma
        
numeros = [ 1, 2, 3, 4, 5]
            
print(sumatoria(numeros))
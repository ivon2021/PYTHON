#8. Análisis final: crea una función que tome una lista 
# y devuelva un diccionario que  tenga la suma total,
# promedio, mínimo, máximo y longitud de la lista.


lista = [35,3,7,10,-7]

def analisis_final (lista):
 
  
 suma = 0
 promedio = 0
 minimo = 0
 maximo = 0
 longitud = 0
    
 for num in lista:
       suma += num
       promedio = suma / len(lista)
       if (minimo == 0 or num < minimo):
            minimo = num
       if (maximo == 0 or num > maximo):
        maximo = num
        longitud = len(lista)
        #return num
 
 print("La suma TOtal es: ", suma)
 print("El promedio es:",promedio)
 print("El minimo es: ", minimo)
 print("El maximo es:", maximo)
 print("La longitud es:", longitud)

analisis_final(lista)



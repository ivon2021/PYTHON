#leyendo un Archivo CSV con  csv.reader 

# importamos el modulo CSV y despues abrimos nuestro archivo CSV como File.
#Definimos el objeto lector y usamos el metodo csv.reader
#para extraer los datos al objeto.
#iteramos sobre el objeto reader y recuperamos cada fila
#de nuestro datos.

#mostramos los datos leidos imprimiesdo sus contenidos
#a la consola, tambien hemos especificado los parametros requeridos 
# tales como: delimiter,quotechas y quoting

import csv
with open('ejemplo.csv') as File:
    reader = csv.reader(File, delimiter=',', 
                        quotechar=',', 
                        quoting = csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
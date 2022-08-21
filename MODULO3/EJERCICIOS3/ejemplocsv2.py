#Escribiendo a un archivo CSV usando  csv.write


import csv

myData = [["Nombre", "Apellido", "Grado"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]

myFile = open('ejemplo2.csv','w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
    
    print('Writing complete')
    
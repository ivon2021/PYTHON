#3.	Escribir un programa que almacene las matrices en una
# lista y muestre por pantalla  su producto.
#Nota: Para representar matrices mediante listas usar 
# listas anidadas, representando  cada vector fila en una lista.


mat1 = ((9, 8, 7),
     (4, 5, 6))

mat2 = ((-4, 0),
     (7, 1),
     (1,1))
resultado = [[0,0],[0,0]]

for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            resultado[i][j] += mat1[i][k] * mat2[k][j]
for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])
    
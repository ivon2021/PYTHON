#1. Impresión en forma regresiva: crea una función que acepte un
# número como  parámetro e imprima en pantalla desde el numero hasta 1.

def Retro(num):
    print("num",num)
    while num >1:
        num -=1
        print(num)
        
Retro(8)
    
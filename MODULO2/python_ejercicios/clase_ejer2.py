#1.-basico: imprime todos los enteros del 0 al 150

#for  i in range(151):
 #   print(i)
 
#2.-multiplos de cinco: imprime todos los multiplos de 5 de 5 a 1000

#for i in range(1001):
 #   if(i%5==0 and i!=0):
  #      print(i)
  
#3.-contar, Dojo Way-imprime enteros del 1 al 100.
#si es divisible por 5, imprima "Coding" en su lugar.
# si es divisible por 10, imprima "Coding Dojo".

 # for i in range(101):
   #   if(i%5 ==0):
  #        print("Coding div 5 i=" ,i)
  #   if(i%10==0):
 #     print("Coding dojo div 10 i=" ,i)

#4.-¡uf!, eso es bastante grande!: suma enteros
# impares de 0 a 500000 e imprime la suma final

#suma=0
#for i in range(500001):
   # if(i%2 !=0):
   #     suma=suma+i
   #     print(suma)
    
    
#5.-cuenta regresiva por cuatro: imprime numeros positivos del 
# 2018 al 0, restando 4 en cada iteracion.

#def retrosede(num):
   # print ("num",num)
    #while num>2:
    #    num -=4
    #    print("num",num)
        
#retrosede(2018)
#print("num 0")

#6.-contador flexible: establece 3 variables: lowNum,highNum,mult.
#comenzando en lowNum y pasando por highNum, imprima solo los enteros
#que son multiplos de mult. por ejemplo, si lowNum=2,


lowNum =  2
highNum  =  9
multi  =  3

for  f  in range( lowNum , highNum  +  1 ):
   if f  %  multi  ==  0 :
     print( f )
    
     #3 6 9



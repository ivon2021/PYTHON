#def a():
 #   b = 100
  #  print(b)
  #  if b < 10:
 #       return 5
  #  else:
   #     return 10
 #   return 7
#print(a())
# salida: 100-10


#Considere el siguiente código:

#b = 500
#print(b)
#def a():
   # b = 300
   # print(b)
#print(b)
#a()
#print(b)

#salida:500 500 300 500

#Considere el siguiente código:

#def a():
 #   print(1)
 #   b()
 #   print(2)
#def b():
  #  print(3)
#a()
#¿Cuál es la salida? 1 3 2 

#Considere el siguiente código:

#def a():
  #  print(1)
  #  x = b()
  #  print(x)
 #   return 10
#def b():
 #   print(3)
 #   return 5
#y = a()
#print(y)
#¿Cuál es la salida?  1 3- 5 -10


#prueba3
#Considere el siguiente código:

#def a():
   # return 5
   # return 10
#print(a())
#La salida es: 5

#Considere el siguiente código:

#def a():
  #  print(5)
#x = a()
#print(x)
#La salida es: 5 none

#Considere el siguiente código:

#def a(b,c):
  #  return str(b)+str(c)
#print(a(2,5))
#La salida es: 25

#Considere el siguiente código:

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#La salida es: 7-14-21
#4. Valores mayores que el segundo: 
# escribe una función que acepte una lista y
# crea  una nueva lista con el valor mínimo,
# máximo y el promedio de la lista original.
def valores():
    
    nums=[]
  
    print("cuantos numeros ingresaras?:")
    n=int(input())
    
    
    i=0
    mayor=0
    menor=0
    
    while i< n:
        print("valor numeros:",i+1)
        val = float(input())  
        nums.append(val)
        i+=1
       
    prom = sum(nums) / len(nums)
    print("El promedio es: ",prom) 
    
    mayor=max(nums)
    menor=min(nums) 
    print("El mayor es: ",mayor)
    print("El menor es: ",menor)
    
    
     
valores()   

    
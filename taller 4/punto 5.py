"""
entrada
suelto=>int=>su
ventas departamento 1=>int=>dep1
ventas departamento 2=>int=>dep2
ventas departamento 3=>int=>dep3
salida
sueldo total al final del mes 3 departamentos=>int=> total3dep
"""
su=int(input("ingrese sueldo "))
dep1=int(input("ingrese ventas echas "))
dep2=int(input("ingrese ventas echas "))
dep3=int(input("ingrese ventas echas "))

ventotal=(dep1+dep2+dep3)
print("venta total: "+str(ventotal))
ex33=(ventotal*33)/100

if(dep1>ex33):
    dep1=su+su*.20/100
else:
    dep1=su  
print("los vendedores del departamento 1 recibiran: "+str(dep1))    
    
if(dep2>ex33):
    dep2=su+su*.20/100
else:
    dep2=su    
print("los vendedores del departamento 2 recibiran: "+str(dep2))    
if(dep3>ex33):
    dep3=su+su*.20/100
else:
    dep3=su        
print("los vendedores del departamento 3 recibiran: "+str(dep3))        



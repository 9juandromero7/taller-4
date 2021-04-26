"""
entrada
salario=>int=>lsal
categoria=>int=>cat
salida
categoria 
sueldo bruto nuevo
categoria fina
"""
sal=int(input("ingrese salario:") )
cat=int(input("ingrese categoria: "))

if (cat==1):
    aumento=sal*.10
if (cat==2):
    aumento=sal*.15
if (cat==3):
    aumento=sal*.20
if (cat==4):
    aumento=sal*.40
if (cat==5):
    aumento=sal*.60    
salario_nuevo=sal+aumento
print("valor del aumento: "+str(aumento)) 
print("sueldo nuevo"+str(salario_nuevo))
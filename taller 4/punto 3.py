"""
entrada
dato1=>int=>a
dato2=>int=>b
dato3=>int=>c
dato4=>int=>d
salida
calcular la siguiente expresion
"""
a=int(input("digite un numero entero: "))
b=int(input("digite un numero entero: "))
c=int(input("digite un numero entero: "))
d=int(input("digite un numero entero: "))

if (d==0):
    form1=(a-c)**2
    print("la respuesta es: "+str(form1))
else:
    print("no es la respuesta correcta") 
    
if (d>=0):
    form2=(a-b)**3/d
    print("la respuesta es: "+str(form2))
else:
    print("no es posible dividir en 0")    
    
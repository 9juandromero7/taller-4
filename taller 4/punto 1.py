"""
entrada=
cantidad invertida=>float=>cain

salida=
dinero final=>float=>dinfi
"""
cain=float(input("digite cantidad a invertir "))
tain=float(input("digite tasa de interes "))

interes=((cain*tain)/100)

if (interes> 100000):
    print("la cantidad generada por el interes es de: " ,(interes), " supera los 100000 ")
elif(interes< 100000):
    print("la cantidad generada por el interes es de: " ,(interes), " no supera los 100000 ")
total=(cain+interes)
print("el saldo total de la cuenta es:",(total))
    



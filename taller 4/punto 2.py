"""
entradas
sueldo=>float=>su
salidas
sueldo final=>float=>sufi
"""
su=float(input("digite sueldo: "))
if su<900000:
    sufi=su*1.15
    print(" aumento un 15% "+str(sufi))
elif su>900000: 
     sufi=su*1.12 
     print(" aumento del 12% "+str(sufi))
     
print("sueldo final = $ "+str(sufi))     
     
    
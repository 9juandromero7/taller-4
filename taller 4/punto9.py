"""
entrada
monto=>int=>mon
salida
monto total a pagar
"""
mon=int(input("ingrese monto: "))

if (mon<=50000)and(mon>=15000):
    print("no hay descuento")
elif (mon >= 50000) and (mon <= 100000):
    des=(mon*.05)/100 
    total=(mon-des)
    print("el descuento es de: "+str(des))
    print("su total a pagar es de: "+str(total))
    print("Juan Diego El Crack")
elif(mon >= 100000) and (mon <= 7000000):
    des=(mon*.11)/100
    total=(mon-des)
    print("el descuento es de: "+str(des))
    print("su total a pagar es de: "+str(total))
    print("Juan Diego El Crack")
elif(mon>=700000) and (mon<=15000000):
    des=(mon*.18)/100
    total=(mon-des)      
    print("el descuento es de: "+str(des))
    print("su total a pagar es de: "+str(total))
    print("Juan Diego El Crack")
elif(mon>=1500000000):
    des=(mon*.25)/100
    total=(mon-des)      
    print("el descuento es de: "+str(des))
    print("su total a pagar es de: "+str(total))
    print("Juan Diego El Crack")
        
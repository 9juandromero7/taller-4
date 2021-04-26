"""
entrada
cantidad de piezas=>int=>canpi
costo refacciones=>int=>core
salida
costo=>int=>cos
inversion=>int=>in
credito=>int=>cre
interes=>int=>int

"""
core=int(input("ingrese costo: "))
canpi=int(input("ingrese cantidad de piezas: "))
total= canpi * core
if total>5000000:
    inversion= total * .55
    banco= total * .30
    credito= total *.15
else:
    inversion=total*.70
    banco=0
    credito=total*.30
 
print("la inversion es de : "+str(inversion)) 
print("prestamo del banco: "+str(banco))  
print("el credito a pagar es: "+str(credito)) 

interes=credito*.20
print("el interes por el credito es:"+str(interes))
    
    
    



"""
entrada=
temperatura=>float=>tem
salida=
tipo de deporte=>str=>td
"""
tem=float(input("digite temperatura: "))
if (tem>85):
    print("natacion")
elif(tem>=71 and tem<=85):
    print("tenis")
elif(tem>=32 and tem<=70):
    print("golf")
elif(tem>=10 and tem<=32):
    print("esqui")
elif(tem<=10):
    print("marcha")
else:
    print("no se encontro un deporte")
    
    
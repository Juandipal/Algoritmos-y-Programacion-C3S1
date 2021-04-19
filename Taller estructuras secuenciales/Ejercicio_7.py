"""
Entradas
Cantidad de metros--->float--->m

Salidas
pulgadas--->float--->inch
pies--->float--->ft
"""
print("CONVERTIDOR DE METROS A SIT. INGLES")
m=float(input("Introduzca el valor en metros: "))
inch=(m*39.27)
ft=(inch/12)
print("El valor en pulgadas es: "+str(inch))
print("El valor en pies es: "+str(ft))
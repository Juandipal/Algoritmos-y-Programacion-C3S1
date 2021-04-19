"""
Entradas

precio final--->float--->pfin
precio de venta--->float--->PVP

Salidas

diferencia--->float--->dif
porcentaje descuento--->float--->desc
"""
print("DESCUENTO APLICADO")
pfin=float(input ("Digite el valor pagado: "))
PVP=float(input ("Ingrese el precio de venta sugerido: "))
dif=(PVP-pfin)
desc=((dif*100)/PVP)
print("El porcentaje de descuento fue: "+str(desc))
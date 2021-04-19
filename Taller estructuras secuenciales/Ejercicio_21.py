"""
Entradas:

precio de contado--->float--->P
valor de la cuota mensual--->float--->T

Salidas:

precio cuotas--->float--->pc
recargo--->float--->r
porcentaje de recargo--->float--->porc
"""
print("COMPARACION PRECIO DE CONTADO Y A CUOTAS")
p=float(input ("Precio de contado:" ))
t=float(input ("Valor de la cuota mensual: "))
pc=(t*12)
r=(pc-p)
porc=((r*100/p))
print("El porcentaje de recargo es: "+str(porc))
"""
Entradas

cantidad de naranjas--->int--->X
precio por docena--->float--->Y
valor venta--->float--->K

salidas

numero de docenas--->float--->doc
costo--->float--->cte
ganancia--->float--->gan
porcentaje ganancia--->float--->porc
"""
X=int(input ("Numero de naranjas compradas: "))
Y=float(input ("Valor por docena: "))
K=float(input ("Valor de las ventas: "))
doc=(X/12)
cte=(Y*doc)
gan=(K-cte)
porc=((gan*100)/cte)
print("El porcentaje de ganancias es: "+str(porc))
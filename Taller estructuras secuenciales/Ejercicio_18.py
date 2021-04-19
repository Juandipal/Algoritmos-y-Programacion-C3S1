"""
Entradas

Capital-->float-->cap
Tiempo--->int--->t
razon--->float--->r

salidas

interes--->float--->i
promedio--->float---prom
"""
cap=float(input ("Digite el valor del capital: "))
t=int(input ("Digite el tiempo de inversion: "))
r=float(input ("Digite la tasa de interes: "))
i=((cap*r*t)/100)
prom=(i/t)
print("El valor del interes es: "+str(i),("El porcentaje anual es: ")+str(prom))
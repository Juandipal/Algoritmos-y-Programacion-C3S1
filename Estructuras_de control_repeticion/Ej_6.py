"""
6.	Efectuar la división de dos números enteros, utilizando el método de las restas sucesivas. Observe el siguiente ejemplo:
Dividir 8 entre 2
"""
dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))
if dividendo>0 and divisor>0:
  cociente=0
  residuo=dividendo
  while (residuo>=divisor):
    residuo-=divisor
    cociente+=1
print(residuo)
print(cociente)

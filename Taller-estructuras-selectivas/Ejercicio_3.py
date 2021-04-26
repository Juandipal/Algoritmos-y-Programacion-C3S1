"""
Entradas
numero 1--->int-->A
numero 2--->int-->B
numero 3--->int-->C
numero 4--->int-->D

Salidas
condicion 1--->float--->c1
condicion 2--->float--->c2
"""
A=int(input ("Digite el valor de A: "))
B=int(input ("Digite el valor de B: "))
C=int(input ("Digite el valor de C: "))
D=int(input ("Digite el valor de D: "))
c1=(A-C)**2
if(D<=0):
  print("El valor es: "+str(c1))
else:
  c2=((A-B)**3)/D
  print("El valor es: "+str(c2))
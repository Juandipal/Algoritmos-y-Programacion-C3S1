"""
Entradas

num 1--->int--->P
num 2--->int--->Q

Salidas:
condicion 1--->str--->c1
condicion 2--->str-->c2
"""
P=int(input("P: "))
Q=int(input("Q: "))
c=(P**3+Q**4-2*P**2)
if(c>680):
  print("P y Q satisfacen la expresión "+str(c))
else:
  print("P y Q no Satisfacen la expresión "+str(c))

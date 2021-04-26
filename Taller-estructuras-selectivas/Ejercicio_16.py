"""
Entradas:
a-->int-->A
b-->int-->B
c-->int--->C
D-->int-->D

Salidas:
x1-->float-->x
x2-->float-->z
"""
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
D=((b**2)-4*a*c)
if(D==0):
  x=(-b/2*a)
  print("La solución única es: "+str(x))
elif (D>0):
  x=((-b)+((b**2-(4*a*c))/(2*a))**0.5)
  z=((-b)-((b**2- (4*a*c))/(2*a))**0.5)
  print("X1: "+str(x)+(" X2: ")+str(z))
elif (D<0):
  print("No tiene solución en los reales")
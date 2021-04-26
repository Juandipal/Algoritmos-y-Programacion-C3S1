"""
Entradas
importe global--->float--->ig
sueldo base--->float--->sb
venta dep 1--->float--->v1
venta dep 2--->float--->v2
venta dep 3--->float--->v3

Salidas
sueldo 1--->float--->sv1
sueldo 2--->float--->sv2
sueldo 3--->float--->sv3
"""
ig=float(input ("Digite el importe global: "))
sb=float(input("Digite el sueldo basico: "))
v1=float(input("Digite el valor de las ventas del departamento 1: "))
v2=float(input("Digite el valor de las ventas del departamento 2: "))
v3=float(input("Digite el valor de las ventas del departamento 3: "))
porc1=((v1*100)/ig)
porc2=((v2*100)/ig)
porc3=((v3*100)/ig)
stot=(sb+(sb*0.2))
if(porc1>33):
  print("Salario del vendedor 1: "+str(stot))
else:
  print("Sueldo vendedor 1: "+str(sb))
if(porc2>33):
  print("Salario vendedor 2: "+str(stot))
else:
  print("Sueldo vendedor 2: "+str(sb))
if(porc3>33):
  print("Salario vendedor 3: "+str(stot))
else:
  print("Sueldo vendedor 3: "+str(sb))
"""
Entradas
Salario bruto--->float--->sbase

Salidas:
salario neto--->float---snet
"""
sbase=float(input("Digite salario bruto: "))
if(sbase<900000):
  aum=(sbase+(sbase*0.15))
  print("El salario neto es: "+str(aum))
else:
  snet=sbase+(sbase*0.2)
  print("El sueldo neto es: "+str(snet))

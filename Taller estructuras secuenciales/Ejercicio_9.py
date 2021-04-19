"""
Entradas:
Horas trabajadas--->float--->horast
precio--->float--->p

Salidas:
Salario bruto--->float--->sbrut
descuentos--->float--->desc
salario neto--->float--->snet
"""
print("CALCULADORA DE SALARIO")
horast=float(input("Ingrese el número de horas trabajadas: "))
p=float(input("Ingrese el valor por cada hora de trabajo: "))
sbrut=(horast*p)
desc=(sbrut*0.2)
snet=(sbrut-desc)
print("El salario neto del trabajador es: "+str(snet))
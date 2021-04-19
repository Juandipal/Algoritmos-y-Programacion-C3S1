"""
Entradas
nombre--->str--->nombre
horas normales trabajadas--->float--->hnt
valor hora normal--->float--->vhn
horas extra trabajadas--->float--->het
numero hijos--->int--->hijos
Salidas

valor horas trabajadas--->float--->pht
precio hora extra trabajada--->float--->phet
sueldo base--->float--->sbase
deducciones--->float-deducc
asignaciones--->float--->asig
sueldo neto--->float--->snet
"""
print("CALCULADORA DE SALARIO DE UN TRABAJADOR")
nombre=str(input("Nombre del trabajador: "))
hnt=float(input("Horas normales trabajadas: "))
vhn=float(input("Valor de la hora normal: "))
het=float(input("horas extra trabajadas: "))
pht=(hnt*vhn)
phet=(het*(vhn*1.25))
sbase=(phet+pht)
deducc=(sbase*0.14)
print("Sueldo base: "+str(sbase))
print("Total deducciones: "+str(deducc))
hijos=int(input("Numero de hijos del trabajador: "))
asig=(250000+(hijos*173000)+180000)
print("Total asignaciones: "+str(asig))
snet=(sbase+asig-deducc)
print("El sueldo neto es: "+str(snet))
""""
entradas
MATEMATICAS
Examen matem--->float--->mathex
tarea 1--->float--->math1
tarea 2--->float--->math2
tarea 3--->float--->math3

FISICA
examen fisica--->float--->phyex
tarea 1--->float--->phy1
tarea 2--->float--->phy2

QUIMICA
examen quimica--->float--->chemex
tarea 1--->float--->chem1
tarea 2--->float--->chem2
tarea 3--->float--->chem3

Salidas
Promedio matematicas--->float--->avmath
promedio fisica--->float--->avphy
promedio quimica--->float--->avchem
promedio general--->float-promg
"""
print("CALCULADORA DE PROMEDIOS")
print("MATEMATICAS")
mathex=float(input("Ingrese nota del examen: "))
math1=float(input("Nota de la tarea 1: "))
math2=float(input("Nota de la tarea 2: "))
math3=float(input("Nota de la tarea 3: "))
avmath=(mathex*0.9)+(((math1+math2+math3)/3)*0.1)
print("FISICA")
phyex=float(input("Ingrese nota del examen: "))
phy1=float(input("Nota de la tarea 1: "))
phy2=float(input("Nota de la tarea 2: "))
avphy=(phyex*0.8)+(((phy1+phy2)/2)*0.2)
print("QUIMICA")
chemex=float(input("Ingrese nota del examen: "))
chem1=float(input("Nota de la tarea 1: "))
chem2=float(input("Nota de la tarea 2: "))
chem3=float(input("Nota de la tarea 3: "))
avchem=(chemex*0.85)+(((chem1+chem2+chem3)/3)*0.15)
promg=((avmath+avphy+avchem)/3)
print("PROMEDIO MATEMATICAS: "+str(avmath))
print("PROMEDIO FISICA: "+str(avphy))
print("PROMEDIO QUIMICA: "+str(avchem))
print("PROMEDIO GENERAL: "+str(promg))
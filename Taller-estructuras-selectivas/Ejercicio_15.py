"""
Entradas:
edad-->int-->edad
hemoglobina-->float-->hemo
sexo-->int--->sexo
Salidas:
anemia-->str
mujerohombre-->str
"""
edad=int(input("Ingresar el valor de edad (meses):"))
hemo=float(input("Ingresa el valor de nivel de hemoglobina:"))
sexo=int(input("Ingrese su sexo (F)=0 (M)=1: "))
if(sexo==0):
 print("F")
else:
 print("M")

if (edad>0 and edad<=1 and hemo<13):
    print("Paciente con anemia")
elif (edad>1 and edad<=6 and hemo<10):
    print("Paciente con anemia")
elif (edad>6 and edad<=12 and hemo<11):
    print("Paciente con anemia")
elif (edad>12 and edad<=60 and hemo<11.5):
    print("Paciente con anemia")
elif (edad>60 and edad<=120 and hemo<12.6):
    print("Paciente con anemia")
elif (edad>120 and edad<=180 and hemo<13):
    print("Poaciente con Anemia")
elif (edad>180 and sexo==1 and hemo<12):
    print("Mujer con anemia")
elif (edad>180 and sexo==0 and hemo<14):
    print("Hombre con anemia")
else:
    print("Negativo para anemia")


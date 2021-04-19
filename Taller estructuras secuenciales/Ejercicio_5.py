"""
Entradas
parcial--->float--->p1
parcial2--->float--->p2
parcial3-->float--->p3
examen final--->float--->ex
trabajo final--->float--->tf

Salidas
promedio examenes--->float--->promp
promedio final--->float--->pf

"""
print("CALCULADORA DE NOTAS PROGRAMACION")
p1=float(input("Digite la calificacion del parcial 1: "))
p2=float(input("Digite la calificacion del parcial 2: "))
p3=float(input("Digite la calificacion del parcial 3: "))
promp=((p1+p2+p3)/3)
ex=float(input ("Digite calificacion del examen final: "))
tf=float(input("Digite la calificacion del trabajo final: "))
pf=((promp*0.55)+(ex*0.3)+(tf*0.15))
print("la calificación final es: "+str(pf))
print("¡SIGA PROGRAMANDO!")
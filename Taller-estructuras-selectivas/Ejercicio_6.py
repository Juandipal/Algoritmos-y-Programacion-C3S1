"""
Entradas

numero 1-->int--->A
numero 2-->int--->B
numero 3-->int--->C
numero 4-->int--->D

Salidas

numero redondeado--->int--->nr
"""

A=int(input("A: ")) 
B=int(input("B: "))
C=int(input("C: "))
D=int(input("D: "))
if(C>5):
  C=0
  D=0
  B=B+1
elif(C<5):
  C=0
  D=0
elif(C==5):
  D=0
N1=A
N2=B
N3=C
N4=D
print("Redondeo: "+str(N1)+str(N2)+str(N3)+str(N4))

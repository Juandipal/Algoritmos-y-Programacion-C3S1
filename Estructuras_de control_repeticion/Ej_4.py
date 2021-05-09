"""
4.	Calcular el término doceavo y la suma de los doce primeros términos de la sucesión: 6, 11, 16, 21. Respuesta: a12=61, suma=402.
"""

lista=[]
for i in range(1,13):
  t=5*i+1
  lista.append(t)
print(lista)
suma=sum(lista)
print(suma)

"""
suma=0
for i in range(1,13):
  t=5*i+1
  suma=suma+t
print(suma)
"""
"""
lista=[]
for i in range(1,13):
  t=5*i+1
  lista.append(t)
suma=0  
for i in lista:
  suma=suma+i
print(suma)
"""
"""
contador=1
suma=0
while (contador<=12):
  t=5*contador+1
  suma=suma+t
  contador=contador+1
print(suma)  
"""
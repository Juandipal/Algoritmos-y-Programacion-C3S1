"""
1.	Sea N y K dos enteros positivos, con K < N. Se desea escribir un programa que escriba el valor de N,N­1,N­2,..., y así sucesivamente hasta llegar al valor de K.

Entradas
K--->int
N--->int

Salidas
Kn---> int--->Valor de K
"""
N=int(input("N: "))
K=int(input("K: "))
Nn=N+1
while (N>K):
  lista=[]
  for i in range (K,Nn):
    lista.append(i)
  lista.sort(reverse=True)
  print(lista)
  break
else:
  print("K debe ser menor que N")
  
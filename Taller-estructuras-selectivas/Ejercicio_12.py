"""
Entradas

cantidad de dinero--->int--->cap

Salidas
100.000 COP--->int--->k100
50.000 COP--->int--->k50
20.000 COP--->int-->k20
10.000 COP--->int--->k10
5.000 COP--->int--->k5
2.000 COP--->int--->k2
1.000 COP--->int--->k1
500 COP--->int--->m500
200 COP--->int--->m200
100 COP--->int--->m100
50 COP--->int--->m50
"""
import math
cap=int(input("Digite valor: "))
umil = cap / 1000
tmp = cap % 1000
centenas = tmp / 100
tmp = tmp % 100
decenas = tmp / 10
unidades = tmp % 10
mil=math.trunc(umil)
c=math.trunc(centenas)
d=math.trunc(decenas)
u=math.trunc(unidades)
if(d>5):
  d=0
  u=0
  c=c+1
elif(d<5):
  d=0
  u=0
elif(d==5):
  u=0
a=mil*1000
b=c*100
c=d*10
if(a>=1000):
  if(a==5000):
    print(5000)
  elif(a==4000):
      print(2000)
      print(2000)
  elif(a==3000):
      print(2000)
      print(1000)
  elif(a==2000):
      print(2000)
  else:
      print(1000)
if(b<=950):
  if(b==900):
    print(500)
    print(200)
    print(200)
  elif(b==800):
    print(500)
    print(200)
    print(100)
  elif(b==700):
    print(500)
    print(200)
  elif(b==600):
    print(500)
    print(100)
  elif(b==500):
    print(500) 
  elif(b==400):
    print(200)
    print(200)
  elif(b==300):
    print(200) 
    print(100) 
  elif(b==200):
    print(200) 
  elif(b==100):
    print(100)                  
if(c==50):
    print(50)
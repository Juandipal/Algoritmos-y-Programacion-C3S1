"""
Desarrolle un programa en Python que calcule y muestre el monto que debe pagar ar suscriptor por concepto de consumo de luz eléctrica y servicio de aseo urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior y la lectura actual por el costo de cada Kilovatio hora, según la siguiente escala:
0 ­ 1004.600 COP/ Kwh
101 ­ 30080.00 COP/ Kwh
301 – 500 100.000 COP /Kwh
501 – en Adelante 120.000 COP/ Khw

Entradas
lectura actual--->float--->lact
lectura anterior--->float--->lant

Salidas
valor factura--->float--->valor
"""
lact=float(input("lectura actual: "))
lant=float(input("lectura anterior: "))
consumo=(lact-lant)
if(consumo>=0 and consumo<=100):
  valor=(consumo*4600)
  print("Valor: "+str(valor))
elif(consumo>=101 and consumo<=300):
  valor=(consumo*80000)
  print("Valor: "+str(valor))
elif(consumo>=301 and consumo<=500):
  valor=(consumo*100000)
  print("Valor: "+str(valor))
elif(consumo>=501):
  valor=(consumo*120000)
  print("Valor: "+str(valor))  
"""
ENTRADAS
Numero de piezas--->int--->piezas
valor unitario--->float--->precio

SALIDAS 
Valor compra--->float--->valor
dinero propio--->float-->propio
credito banco--->float--->banco
credito fabricante--->fab
interes-->float--->i
"""
piezas=int(input ("Ingrese el numero de piezas compradas: "))
precio=float(input ("Ingrese el valor de cada pieza: "))
valor=(piezas*precio)
if(valor<=5000000):
  propio=(valor*0.7)
  fab=(valor*0.3)
  i=(fab*0.2)
  print(("El valor a pagar con dinero de la empresa es: "+str(propio)))
  print(("El valor del credito sera: "+str(fab)))
  print("El valor del interes es: "+str(i))
else:
  propio=(valor*0.55)
  fab=(valor*0.15)
  i=(fab*0.2)
  banco=(valor*0.3)
  print(("El valor a pagar con dinero de la empresa es: "+str(propio)))
  print(("El valor del credito sera: "+str(fab)))
  print("El valor del interes es: "+str(i))
  print("El monto a solicitar al banco es: "+str(banco))
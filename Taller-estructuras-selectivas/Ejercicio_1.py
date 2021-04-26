"""
Entradas
Capital--->float-->cap
tasa interes--->float--->i

Salidas
ganancia--->float--->gan
ganancia si reinvierte--->float--->fin
"""
cap=float(input("Ingrese el capital invertido: "))
i=float(input ("Digite la tasa de interes: "))
gan=cap*(i/100)
fin=((gan+cap)*i)
if(gan<100000):
  print("El valor de las ganancias es: "+str(gan))
else:
  print("El valor final en la cuenta será: "+str(fin))


"""
en una tienda efectúan un descuento a los clientes dependiendo del monto de la compra. El descuento se efectúa con base en el siguiente criterio:
a.	Si el monto es inferior a $50.000 COP, no hay descuento.
b.	Si está comprendido entre $50.000 COP y $100.000 COP inclusive, se hace un descuento del 5%
c.	Si está comprendido entre $100.000 COP y $700.000 COP inclusive, se hace un descuento del 11%
d.	Si está comprendido entre $700.000 COP y $1.500.000 COP inclusive, el descuento es del 18
e.	Si el monto es mayor a $1500000, hay un 25% de descuento.

Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar y descuento recibido.

Entradas

nombre--->str--->name
monto compra--->float--->price

Salidas
monto a pagar--->float--->net
descuento--->float--->desc
"""
name=str(input("Nombre del cliente: "))
price=float(input("Monto de la compra: "))
if(price>0 and price<=50000):
  net=(price-(price*0.05))
  desc=(price-net)
  print("Nombre: "+str(name)+(" Monto de la compra: "+str(price)+(" Descuento: ")+str(desc)+" Valor neto: "+str(net)))
elif(price>50000 and price<=100000):
  net=(price-(price*0.11))
  desc=(price-net)
  print("Nombre: "+str(name)+(" Monto de la compra: "+str(price)+(" Descuento: ")+str(desc)+" Valor neto: "+str(net)))
elif(price>100000 and price<=700000):
  net=(price-(price*0.18))
  desc=(price-net)
  print("Nombre: "+str(name)+(" Monto de la compra: "+str(price)+(" Descuento: ")+str(desc)+" Valor neto: "+str(net)))
elif(price>1500000):
  net=(price-(price*0.25))
  desc=(price-net)
  print("Nombre: "+str(name)+(" Monto de la compra: "+str(price)+(" Descuento: ")+str(desc)+" Valor neto: "+str(net)))
""""
entradas
lectura actual--->float--->lact
lectura anterior--->float--->lant
valor kw--->float--->kwh

salidas
consumo--->float--->cons
total factura-->float--->total
"""
print("FACTURA DE ENERGIA ELECTRICA")
lact=float(input ("Digite lectura actual: "))
lant=float(input ("Digite lectura anterior: "))
kwh=float(input ("Valor del kilowatio: "))
cons=(lact-lant)
total=(cons*kwh)
print("El valor a pagar es :"+str(total))
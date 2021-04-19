"""
Entradas
Compra total-->int--->ct

Salidas
Descuento aplicado--->float--->desc
"""
print("CALCULADORA DE DESCUENTOS")
ct=int(input("Digite el valor de la compra total: "))
desc=(ct*0.15)
print("El descuento aplicado es: "+str(desc))
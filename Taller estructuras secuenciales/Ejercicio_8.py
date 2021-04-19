""""
Entradas
lado 1--->float--->a
lado 2--->float--->b
lado 3--->float--->c

Salidas
semiperimetro--->float--->s
area--->float--->A

"""
print("Calculadora de area de triangulos")
print("Introduzca los valores de los lados: ")
a=float(input("Valor del lado 1: "))
b=float(input("Valor del lado 2: "))
c=float(input("Valor del lado 3: "))
s=((a+b+c)/2)
A=((s*(s-a)*(s-b)*(s-c))**0.5)
print("El area del triangulo es: "+str(A))
""""
Entradas
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->V2
Sueldobase-->float-->sb
Salidas
comision-->float-->c
sueldototal-->float->total    
"""
v1=float(input("Digite el valor de la venta 1: "))
v2=float(input("Digite el valor de la venta 2: "))
v3=float(input("Digite el valor de la venta 3: "))
sb=float(input("Digite el valor del sueldo base: "))
c=((v1+v2+v3)/3)*0.10
total=sb+c
print("La comisión es: "+str(c)," Sueldo total: "+str(total))
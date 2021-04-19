"""
entradas:

Presupuesto total--->float--->ptotal
porcentajes de presupuesto por area ya estan establecidos: (40% ginecologia, 30% traumatologia, 30% pediatria)

Salidas
presupuesto ginecologia--->float--->pgin
presupuesto traumatologia--->float--->ptrau
presupuesto pediatria--->float--->pped
"""
print("PRESUPUESTO POR AREAS DEL HOSPITAL")
ptotal=float(input ("Digite el valor del presupuesto total anual "))
pgin=(ptotal*0.4)
ptrau=(ptotal*0.3)
pped=(ptotal*0.3)
print("El presupuesto de ginecologia sera: "+str(pgin))
print("El presupuesto de traumatologia sera: "+str(ptrau))
print("El presupuesto de pediatria sera: "+str(pped))
"""
Entradas:
Temperatura--->float--->temp

Salidas

tipo de deporte-->str--->tipo
"""
t=float(input ("Digite la temperatura: "))
if(t>85):
  print("Natación")
elif(t>71 and t<=85):
  print("Tennis")
elif(t>33 and t<=70):
  print("Golf")
elif(t>10 and t<=32):
  print("Esqui")
elif(t<=10):
  print("Marcha")
else:
 print("No se identifico deporte")
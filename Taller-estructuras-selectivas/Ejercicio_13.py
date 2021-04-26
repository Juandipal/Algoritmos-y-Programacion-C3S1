"""
Entradas
fecha nacimiento--->date
Salidas
signo--->str--->sign
edad--->str--->edad
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

day=int(input("día de nacimiento: "))
month=int(input("mes de nacimiento: "))
year=int(input("año de nacimiento: ")) 
fechan=(str(day)+("/")+str(month)+("/")+str(year))
print("Su fecha de nacimiento es: "+str(fechan))
if((month==11) and (day>=22)) or ((month==12) and (day<=21)):
   print("Sagitario") 
if((month==12) and (day>=22)) or ((month==1) and (day<=20)):
  print("Capricornio") 
if((month==1) and (day>=21)) or ((month==2) and (day<=19)):
  print("Acuario")
if((month==2) and (day>=20)) or ((month==3) and (day<=19)):
 print("Psicis") 
if((month==3) and (day>=21)) or ((month==4) and (day<=20)):
  print("Aries")
if((month==4) and (day>=21)) or ((month==5) and (day<=21)):
  print("Tauro") 
if((month==5) and (day>=22)) or ((month==6) and (day<=21)):
  print("Geminis")
if((month==6) and (day>=22)) or ((month==7) and (day<=22)):
  print("Cancer")
if((month==7) and (day>=23)) or ((month==8) and (day<=23)):
 print("Leo")
if((month==8) and (day>=24)) or ((month==9) and (day<=22)):
  print("virgo") 
if((month==9) and (day>=23)) or ((month==10) and (day<=22)):
  print("Libra")
if((month==10) and (day>=23)) or ((month==11) and (day<=21)):
  print("Escorpion")
birthday= datetime.strptime(fechan, "%d/%m/%Y")
edad=relativedelta(datetime.now(), birthday)
print(f"{edad.years} años, {edad.months} meses y {edad.days} dias")
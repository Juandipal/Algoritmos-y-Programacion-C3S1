"""
Entradas

N1--->int
N2--->int
N3--->int
N4--->int
N5--->int
N6--->int
N7--->int
N8--->int

salidas
Dinero total en el banco--->int--->total
"""
print("DINERO TOTAL EN UN BANCO")
N1=int (input ("Numero de billetes de $50.000 "))
N2=int (input ("Numero de billetes de $20.000 "))
N3=int (input ("Numero de billetes de $10.000 "))
N4=int (input ("Numero de billetes de $5.000 "))
N5=int (input ("Numero de billetes de $2.000 "))
N6=int (input ("Numero de billetes de $1.000 "))
N7=int (input ("Numero de billetes de $500 "))
N8=int (input ("Numero de billetes de $100 "))
total=((N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100))
print("La cantidad de dinero en el banco es: " +str(total))
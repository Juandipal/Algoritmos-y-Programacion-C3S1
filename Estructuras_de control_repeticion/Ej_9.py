Alcool=0
Gasolina=0
Diesel=0
while(1):
    x=int(input())
    if(x==4):
        break
    elif(x==1):
        Alcool+=1
    elif(x==2):
        Gasolina+=1
    elif(x==3):
        Diesel+=1
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool:", Alcool)
print("Gasolina:", Gasolina)
print("Diesel:", Diesel)
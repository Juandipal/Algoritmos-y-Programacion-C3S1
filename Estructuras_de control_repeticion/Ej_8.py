while(True):
 try:
  s=int(input())
  if(s==2002):
    print("Acesso Permitido")
    break
  else:
    print("Senha Invalida")
 except EOFError:
     break
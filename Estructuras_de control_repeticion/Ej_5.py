"""	Calcule e imprima el número de términos necesarios para que el valor de la siguiente sumatoria se aproxime los más cercanamente a 1000 sin que lo exceda:
∑((k**2+1)/k, donde k=1,2,3,4,...
"""

for k in range(1,1001):
  sigma=(k**2+1)/k
  if(sigma>=999):
    break
print(sigma,k)
  
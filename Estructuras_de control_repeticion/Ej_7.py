"""
Entradas

M--->int
X--->int

Salidas

E--->int
"""
while True:
    X, M=map(int, input().split())
    if X==0 and M==0:
        break
    E=X*M
    print(E)
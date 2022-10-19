from math import isqrt

def perfecto(n):
    divisores = []
    m = 0

    for i in range(1, isqrt(n)):
        if n%i == 0:
            divisores.append(i)
            m = m + i

    for i in divisores:
        divisores.append(n/i)
        m = m + n/i
    
    if isqrt(n) == divisores[-1]:
        m = m - isqrt(n)
        print("tiene raiz")
    
    print(divisores)

    if sum(divisores) == n:
        print("es perfecto")
    else:
        print("no es perfecto")

perfecto(6)
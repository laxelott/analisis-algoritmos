from math import ceil

def perfecto(n):
    m = 0

    for i in range(1, ceil(n/2)+1):
        if n%i == 0:
            m += i

    if m == n:
        return True
    else:
        return False

def mostrarPerfectos(n):
    m = 0
    i = 0
    while m <= n:
        if perfecto(i):
            m = m + 1
            print(f"Perfecto #{m}: {i}")
        i += 1

mostrarPerfectos(10)
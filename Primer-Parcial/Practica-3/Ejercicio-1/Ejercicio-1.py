import random
import pandas as pd

def division1(n, div, res):
    q = 0
    while n >= div:
        n = n-div
        q = q+1
    res = n
    return q

def division2(n, div, res):
    dd = div
    q = 0
    r = n
    while dd <= n:
        dd = 2*dd
    while dd > div:
        dd = dd/2
        q = 2*q
        if dd <= r:
            r = r-dd
            q = q+1
    return q

def division3(n, div, res):
    if div > n:
        return 0
    else:
        return 1 + division3(n-div, div, res)

def analisisDivision(n, fileName):
    global contador
    res1 = []
    res2 = []
    res3 = []

    for i in range(1, n):
        n1 = random.randint(i*5 + 1, i*10)
        n2 = random.randint(0, i*5)
        print(f"Paso: {i} ({n1}, {n2})", end='')

        contador = 0
        print(" -Division 1", end='')
        division1(n1, n2, 0)
        res1.append(contador)

        contador = 0
        print(" -Division 2", end='')
        division2(n1, n2, 0)
        res2.append(contador)

        contador = 0
        print(" -Division 3", end='\n')
        division3(n1, n2, 0)
        res3.append(contador)
    
    print("Escribiendo a csv...")

    df = pd.DataFrame()
    df['Divison1'] = pd.Series(res1)
    df['Divison2'] = pd.Series(res2)
    df['Divison3'] = pd.Series(res3)

    df.to_csv(fileName)

analisisDivision(5000, "division.csv")
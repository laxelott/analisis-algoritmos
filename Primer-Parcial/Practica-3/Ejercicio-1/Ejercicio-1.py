import random
import pandas as pd

def division1(n, div, res):
    global contador
    contador += 1
    q = 0
    while n >= div:
        contador += 1
        contador += 1
        n = n-div
        contador += 1
        q = q+1
    contador += 1
    res = n
    contador += 1
    return q

def division2(n, div, res):
    global contador
    contador += 1
    dd = div
    contador += 1
    q = 0
    contador += 1
    r = n
    while dd <= n:
        contador += 1
        contador += 1
        dd = 2*dd
    while dd > div:
        contador += 1
        contador += 1
        dd = dd/2
        contador += 1
        q = 2*q
        contador += 1
        if dd <= r:
            contador += 1
            r = r-dd
            contador += 1
            q = q+1
    contador += 1
    return q

def division3(n, div, res):
    global contador
    contador += 1
    if div > n:
        contador += 1
        return 0
    else:
        contador += 1
        return 1 + division3(n - div, div, res)

def analisisDivision(n, fileName):
    global contador
    res1 = []
    res2 = []
    res3 = []
    num1 = []
    num2 = []

    for i in range(1, n):
        n1 = random.randint(i*5 + 1, i*10)
        n2 = random.randint(i*2, i*5)
        print(f"Paso: {i} ({n1}, {n2})", end='\n')

        num1.append(n1)
        num2.append(n2)

        contador = 0
        division1(n1, n2, 0)
        res1.append(contador)

        contador = 0
        division2(n1, n2, 0)
        res2.append(contador)

        contador = 0
        division3(n1, n2, 0)
        res3.append(contador)
    
    print("Escribiendo a csv...                 ")

    df = pd.DataFrame()
    # df['n1'] = pd.Series(num1)
    # df['n2'] = pd.Series(num2)
    df['Divison1'] = pd.Series(res1)
    df['Divison2'] = pd.Series(res2)
    df['Divison3'] = pd.Series(res3)

    df.to_csv(fileName)

analisisDivision(20000, "division.csv")
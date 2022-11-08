from math import floor
import numpy as np
import pandas as pd
import random


## ALGORITMO RECURSIVO
def recursivoInicio(arreglo, elemento):
    global contador

    contador += 1
    arreglo.sort()
    contador += 1
    return encuentraRecursivo(arreglo, elemento)

def encuentraRecursivo(arreglo, elemento):
    global contador

    if len(arreglo) < 3:
        contador += 1
        contador += 1
        return False

    contador += 1
    n = floor(len(arreglo) / 3)
    if (arreglo[0] == elemento) or (arreglo[n] == elemento) or (arreglo[2*n] == elemento):
        contador += 1
        contador += 1
        return True
    elif(elemento < arreglo[n]):
        contador += 1
        contador += 1
        arr = arreglo[0:n] 
    elif(elemento < arreglo[n*2]):
        contador += 1
        contador += 1
        arr = arreglo[n:n*2]
    else:
        contador += 1
        arr = arreglo[n*2:n*3]
        
    contador += 1
    return encuentraRecursivo(arr, elemento)

## ALGORITMO ITERATIVO
def iterativoInicio(arreglo, elemento):
    global contador

    contador += 1
    arreglo.sort()
    contador += 1
    return encuentraIterativo(arreglo, elemento)

def encuentraIterativo(arreglo, elemento):
    global contador

    while(len(arreglo) >= 3):
        contador += 1
        contador += 1
        n = floor(len(arreglo) / 3)
        if (arreglo[0] == elemento) or (arreglo[n] == elemento) or (arreglo[2*n] == elemento):
            contador += 1
            contador += 1
            return True
        elif(elemento < arreglo[n]):
            contador += 1
            contador += 1
            arreglo = arreglo[0:n] 
        elif(elemento < arreglo[n*2]):
            contador += 1
            contador += 1
            arreglo = arreglo[n:n*2]
        else:
            contador += 1
            arreglo = arreglo[n*2:n*3]

    contador += 1
    return False

def mejorCaso(arr, elem):
    arr[0] = elem
    return arr

def peorCaso(arr, elem):
    return [elem+1 if x==elem else x for x in arr]

def analisisIterativo(n, fileName):
    global contador
    axis = []
    resNorm = []
    resPeor = []
    resMejor = []

    print("Iniciando análisis de iterativo")
    for i in range(1, n):
        print(f"Paso: {i}", end="\r")
        arr = np.random.randint(0, i*2, size=i)
        elem = random.randint(0, i*2)
        peor = peorCaso(arr, elem)
        mejor = mejorCaso(arr, elem)

        axis.append(i)

        contador = 0
        iterativoInicio(arr, elem)
        resNorm.append(contador)
        
        contador = 0
        iterativoInicio(peor, elem)
        resPeor.append(contador)
        
        contador = 0
        iterativoInicio(mejor, elem)
        resMejor.append(contador)

    print("Escribiendo a csv...")

    df = pd.DataFrame()
    df['Caso Normal'] = pd.Series(resNorm)
    df['Caso Peor'] = pd.Series(resPeor)
    df['Caso Mejor'] = pd.Series(resMejor)

    df.to_csv(fileName)

def analisisRecursivo(n, fileName):
    global contador
    axis = []
    resNorm = []
    resPeor = []
    resMejor = []

    print("Iniciando análisis de recursivo")
    for i in range(1, n):
        print(f"Paso: {i}", end="\r")
        arr = np.random.randint(0, i*2, size=i)
        elem = random.randint(0, i*2)
        peor = peorCaso(arr, elem)
        mejor = mejorCaso(arr, elem)

        axis.append(i)

        contador = 0
        recursivoInicio(arr, elem)
        resNorm.append(contador)
        
        contador = 0
        recursivoInicio(peor, elem)
        resPeor.append(contador)
        
        contador = 0
        recursivoInicio(mejor, elem)
        resMejor.append(contador)

    print("Escribiendo a csv...")

    df = pd.DataFrame()
    df['Caso Normal'] = pd.Series(resNorm)
    df['Caso Peor'] = pd.Series(resPeor)
    df['Caso Mejor'] = pd.Series(resMejor)

    df.to_csv(fileName)

n = 2000
analisisIterativo(n, "iterativo.csv")
analisisRecursivo(n, "recursivo.csv")
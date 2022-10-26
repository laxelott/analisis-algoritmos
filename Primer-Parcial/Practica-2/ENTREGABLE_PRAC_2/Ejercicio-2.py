"""
    INSTITUTO POLITECNICO NACIONAL
    ESCUELA SUPERIOR DE CÓMPUTO
    ALUMNOS:
        - SÁNCHEZ VERDIGUEL ISAAC
        - TREVIÑO PALACIOS AXEL 
    GRUPO: 3CV11
    MATERIA: ANALISIS DE ALGORITMOS
    PROFESOR: BENJAMIN LUNA BENOSO
    FECHA: 26 - 10 - 2022
    PRACTICA 2: COMPLEJIDADES TEMPORALES POLINOMIALES Y NO POLINOMIALES
"""

import csv
from math import ceil


# FUNCIONES PRINCIPALES:
def perfecto(n):
    global contador

    contador += 1
    m = 0

    contador += 1
    for i in range(1, ceil(n / 2) + 1):
        contador += 1
        contador += 1
        if n % i == 0:
            contador += 1
            m += i
    contador += 1

    contador += 1
    if m == n:
        contador += 1
        return True
    else:
        contador += 1
        return False


def mostrarPerfectos(n):
    global contador

    contador += 1
    m = 0
    contador += 1
    i = 0
    while m < n:
        contador += 1
        contador += 1
        print(f"Probando {i}...", end="\r")
        contador += 1
        if perfecto(i):
            contador += 1
            m = m + 1
            contador += 1
            print(f"Perfecto #{m}: {i}")
        contador += 1
        i += 1


# FUNCIONES DE ANÁLISIS:
def analisisPerfecto(lim):
    global contador
    contador = 0
    resultados = []

    print("Análisis de Perfecto:")
    for i in range(0, lim + 1):
        p = perfecto(i)
        print(("si" if p else "no") + " es perfecto")
        print(f"({i}) -> {contador}")
        resultados.append([i, contador])
        contador = 0
    return resultados


def analisisMostrarPerfectos(lim):
    global contador
    contador = 0
    resultados = []

    print("Análisis de Mostrar Perfectos:")
    for i in range(0, lim + 1):
        mostrarPerfectos(i)
        print(f"({i}) -> {contador}")
        resultados.append([i, contador])
        contador = 0
    return resultados


# FUNCIÓN PARA GUARDAR CSV
def guardarResultados(resultados, fileName):
    with open(fileName, "w") as f:
        writer = csv.writer(f)
        for data in resultados:
            writer.writerow(data)


resultados = analisisPerfecto(5000)
guardarResultados(resultados, "data1.csv")
resultados = analisisMostrarPerfectos(6)
guardarResultados(resultados, "data2.csv")

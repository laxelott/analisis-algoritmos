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

# FUNCIONES PRINCIPALES:
import csv


def fibonacci(lim):
    global contador

    contador += 1
    n1 = 1
    contador += 1
    n2 = 1

    # lim - 2 para omitir los dos primeros numeros (porque los dos son 1)
    contador += 1
    for i in range(0, lim - 2):
        contador += 1
        contador += 1
        n2 += n1
        contador += 1
        n1 = n2 - n1
    contador += 1

    contador += 1
    return n2


# FUNCIONES DE ANÁLISIS:
def analisisFibonacci(lim):
    global contador
    contador = 0
    resultados = []

    print("Análisis de Perfecto:")
    for i in range(0, lim + 1):
        print(fibonacci(i))
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


resultados = analisisFibonacci(500)
guardarResultados(resultados, "data.csv")

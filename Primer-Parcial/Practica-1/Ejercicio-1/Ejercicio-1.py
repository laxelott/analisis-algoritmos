import random
import csv

contador = 0 

# GENERADORES
# Genera el arreglo para el caso normal
def generarArreglo(n):
    resultado = []
    for i in range(0, n):
        resultado.append(random.randrange(0, 3*n))
        i += 1
    return resultado

# Genera el arreglo para el mejor caso
def mejorCaso(n):
    arreglo = generarArreglo(n)
    # El cual tiene el mismo elemento al inicio y en la mitad
    arreglo[int(len(arreglo)/2)] = arreglo[0]
    return arreglo

# Genera el arreglo para el peor caso
def peorCaso(n):
    resultado = []
    # El cual no tiene ningún elemento compartido entre las dos mitades (por eso se generan en dos diferentes fors)
    for i in range(0, int(n/2)):
        resultado.append(random.randrange(0, int(1.5*n)))
        i += 1
    for i in range(int(n/2), n):
        resultado.append(random.randrange(int(1.6*n), 3*n))
        i += 1
    return resultado

# ALGORITMO
def detectar(arreglo):
    global contador

    contador += 1
    salir = False

    # Dividir el arreglo en dos mitades
    contador += 1
    result = [False]
    contador += 1
    m1 = arreglo[0 : int(len(arreglo)/2)]
    contador += 1
    m2 = arreglo[int(len(arreglo)/2):len(arreglo)]
    contador += 1
    i = 0
    
    contador += 1
    for e1 in m1:
        contador += 1
        contador += 1
        j = 0
        contador += 1
        # Iteramos la segunda mitad para cada elemento de la primera mitad
        for e2 in m2:
            contador += 1
            # Si se encuentra el elemento en común entonces se guarda y se sale del primer for
            if e1 == e2:
                contador += 1
                contador += 1
                result[0] = True
                contador += 1
                result.append(e1)
                contador += 1
                result.append(i)
                contador += 1
                result.append(j+int(len(arreglo)/2))
                contador += 1
                salir = True
                contador += 1
                break
            contador += 1
            contador += 1
            j += 1
        i += 1
        contador += 1
        contador += 1
        # Si se encontró el elemento en común tambien se sale del segundo for
        if salir:
            contador += 1
            contador += 1
            break
    contador += 1
    return result

resultados = []

for i in range(2, 100):
    arreglo = generarArreglo(i)
    # arreglo = mejorCaso(i)
    # arreglo = peorCaso(i)

    resultado = detectar(arreglo)
    print(arreglo)
    if (resultado[0]):
        print(f"El elemento {resultado[1]} está repetido en [{resultado[2]},{resultado[3]}]")
    else:
        print("Las dos mitades no tienen elementos en común")
    
    resultados.append([i, contador])
    contador = 0

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    for data in resultados:
        writer.writerow(data)
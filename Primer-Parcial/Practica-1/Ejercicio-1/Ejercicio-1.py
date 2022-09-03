import random
import csv

contador = 0 


# GENERADORES
def generarArreglo(n):
    resultado = []
    for i in range(0, n):
        resultado.append(random.randrange(0, 3*n))
        i += 1
    return resultado

def mejorCaso(n):
    arreglo = generarArreglo(n)
    arreglo[int(len(arreglo)/2)] = arreglo[0]
    return arreglo

def peorCaso(n):
    resultado = []
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
        for e2 in m2:
            contador += 1
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
import csv
import math
import random

contador = 0 

def Euclides(m, n) :
    global contador
    
    # Mientras haya un residuo
    while n != 0:
        contador += 1
        # Continuar con el residuo y el segundo número
        contador += 1
        r = m % n
        contador += 1
        m = n
        contador += 1
        n = r
    contador += 1
    return m

resultados = []

# Caso Normal
# En el caso normal se usarán datos al azar entre 2 y el número máximo del peor caso
for i in range(500):
        m = random.randrange(2, 20365011074)
        n = random.randrange(2, 20365011074)
        
        contador = 0
        Euclides(m, n)
        print(f"({m}, {n}) -> {contador}")
        resultados.append([max(m, n), contador])

# Peor caso
# En el peor caso se usan los primeros 50 valores de la serie Fibonacci
# m = n = 1
# for i in range(50):
#     contador = 0
#     Euclides(m, n)
#     print(f"({m}, {n}) -> {contador}")
#     resultados.append([n, contador])
#     n += m
#     m = n - m

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    for data in resultados:
        writer.writerow(data)
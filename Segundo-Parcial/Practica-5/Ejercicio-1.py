"""
    INSTITUTO POLITECNICO NACIONAL
    ESCUELA SUPERIOR DE CÓMPUTO
    ALUMNOS:
        - SÁNCHEZ VERDIGUEL ISAAC
        - TREVIÑO PALACIOS AXEL 
    GRUPO: 3CV11
    MATERIA: ANALISIS DE ALGORITMOS
    PROFESOR: BENJAMIN LUNA BENOSO
    FECHA: 21 - 12 - 2022
    PRACTICA 5: ALGORITMO GREEDY
"""

import math
import random
import pandas as pd
import sys
sys.path.append( './../../' )
from libs.LoadingBar import LoadingBar

def fertilizante(r: int, diasTienda: list):
    global prog
    prog = prog + 1
    prog = prog + 1
    d = 0
    res = []
    prog = prog + 1
    for i in range(len(diasTienda)):
        prog = prog + 1
        prog = prog + 1
        if r + d < diasTienda[i]:
            prog = prog + 1
            prog = prog + 1
            prog = prog + 1
            d = diasTienda[i-1]
            res.append(d)
    prog = prog + 1

    prog = prog + 1
    if len(res) > 0:
        prog = prog + 1
        if res[0] != 0:
            prog = prog + 1
            res.insert(0, 0)
    else:
        prog = prog + 1
        res.insert(0, 0)
        
    prog = prog + 1
    prog = prog + 1
    res.append(diasTienda[-1])
    return res

def analisis_fertilizante(n, fileName):
    global prog
    res = [
        [],[],[],[],[],[],[]
    ]
    eje = []
    loading = LoadingBar(n)
    
    print(f"Realizando {n} casos...")
    loading.start()
    for i in range(5, n+5):
        limite = i*10
        c = random.sample(range(1, limite), i)
        eje.append(i)
        
        # Mejor Caso
        prog = 0
        fertilizante(limite + 1, c)
        res[0].append(prog)

        # Peor Caso
        prog = 0
        fertilizante(0, c)
        res[1].append(prog)
        
        # Azar 5 veces
        for j in range(5):
            prog = 0
            fertilizante(random.randint(0, math.floor(limite/3)), c)
            res[2+j].append(prog)
        
        loading.plusProgress()
    loading.finalize()
    
    print("\nEscribiendo a csv...")
    df = pd.DataFrame()
    df['X'] = pd.Series(eje)
    df['Mejor Caso'] = pd.Series(res[0])
    df['Peor Caso'] = pd.Series(res[1])
    df['Azar1'] = pd.Series(res[2])
    df['Azar2'] = pd.Series(res[3])
    df['Azar3'] = pd.Series(res[4])
    df['Azar4'] = pd.Series(res[5])
    df['Azar5'] = pd.Series(res[6])
    df.to_csv(fileName)
        
analisis_fertilizante(200, "output.csv")
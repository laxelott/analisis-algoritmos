"""
    INSTITUTO POLITECNICO NACIONAL
    ESCUELA SUPERIOR DE CÓMPUTO
    ALUMNOS:
        - SÁNCHEZ VERDIGUEL ISAAC
        - TREVIÑO PALACIOS AXEL 
    GRUPO: 3CV11
    MATERIA: ANALISIS DE ALGORITMOS
    PROFESOR: BENJAMIN LUNA BENOSO
    FECHA: 28 - 12 - 2022
    PRACTICA 6: SECUENCIA COMÚN MÁS LARGA
"""

import random
import sys
import pandas as pd
sys.path.append( './../../' )
from libs.LoadingBar import LoadingBar

def comparar(secuencia1, secuencia2):
    return lcs(secuencia1, secuencia2, len(secuencia1), len(secuencia2))

# Longest Common Sequence
def lcs(sec1, sec2, len1, len2):
    global prog
    prog += 1
    if len1 == 0 or len2 == 0:
        prog += 1
        # Límite
        return 0
    elif sec1[len1-1] == sec2[len2-1]:
        prog += 1
        # Si hay secuencia común, sigue sumando
        return 1 + lcs(sec1, sec2, len1-1, len2-1)
    else:
        prog += 1
        # Si no, sigue buscando
        return max(lcs(sec1, sec2, len1, len2-1), lcs(sec1, sec2, len1-1, len2))

def analisisLCS(n, fileName):
    global prog
    loading = LoadingBar(n)
    res = {
        'mejor': [],
        'peor': [],
        'azar': [
            [], []
        ]
    }
    
    with open('lorem-ipsum.txt') as file:
        lorem = file.read()
    
    print("Ejecutando...")
    loading.start()
    for i in range(n):
        # Generar "archivos" como strings para no desgastar el disco duro
        archivo1 = ''.join(random.sample(lorem[0: i+2], i+2))
        archivo2 = ''.join(random.sample(lorem[0: i+2], i+2))
        
        # Mejor caso (segundo archivo está vacío)
        prog = 0
        comparar(archivo1, '')
        res['mejor'].append(prog)
        
        # Peor caso (los dos archivos son de la máxima longitud)
        prog = 0
        comparar(archivo1, archivo2)
        res['peor'].append(prog)
        
        # Caso al azar (el segundo archivo tiene longitud al azar)
        prog = 0
        comparar(archivo1, archivo2[0: random.randrange(0, i+2)])
        res['azar'][0].append(prog)
        prog = 0
        comparar(archivo1, archivo2[0: random.randrange(0, i+2)])
        res['azar'][1].append(prog)
        
        loading.plusProgress()
    loading.finalize()
    
    print("\nEscribiendo a csv...")
    df = pd.DataFrame()
    df['Mejor Caso'] = pd.Series(res["mejor"])
    df['Peor Caso'] = pd.Series(res["peor"])
    df['Azar1'] = pd.Series(res["azar"][0])
    df['Azar2'] = pd.Series(res["azar"][1])
    df.to_csv(fileName)
    
analisisLCS(15, "output.csv")
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
    PRACTICA EXTRA: GRAFO HAMILTONIANO
"""

from libs.LoadingBar import LoadingBar
import pandas as pd
import sys
sys.path.append('./../../')


class Graph:

    # Constructor
    def __init__(self, edges, n):

        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def hamiltonianPaths(graph, v, visited, path, n):
    global prog

    prog += 1
    # si se visitan todos los vértices, entonces existe el camino hamiltoniano
    if len(path) == n:
        # Imprime el camino hamiltoniano
        print("Es Hamiltoniano")
        prog += 1
        return

    # Comprobar si cada arista a partir del vértice `v` conduce a una solución o no
    prog += 1
    for w in graph.adjList[v]:
        prog += 1

        # Procesa solo vértices no visitados
        prog += 1
        if not visited[w]:
            prog += 1
            prog += 1
            visited[w] = True
            path.append(w)

            # Verificar si agregar el vértice `w` a la ruta conduce a la solución o no
            prog += 1
            hamiltonianPaths(graph, w, visited, path, n)

            # retractarse
            prog += 1
            prog += 1
            visited[w] = False
            path.pop()
    prog += 1


def findHamiltonianPaths(graph, n):
    global prog
    # comienza con cada nodo
    prog += 1
    for start in range(n):
        prog += 1

        # agregar nodo de inicio a la ruta
        prog += 1
        path = [start]

        prog += 1
        prog += 1
        # marcar el nodo de inicio como visitado
        visited = [False] * n
        visited[start] = True

        prog += 1
        hamiltonianPaths(graph, start, visited, path, n)
    prog += 1


def generateAllEdges(v):
    edges = []
    for i in range(v):
        for j in range(i+1, v):
            edges.append((i, j))
    return edges


def analisisHamilton(n, fileName):
    global prog
    global loading
    loading = LoadingBar(n)
    res = {
        'ejes': [],
        'prog': []
    }

    loading.start()
    for i in range(2, n+2):

        edges = generateAllEdges(i)
        graph = Graph(edges, i)

        prog = 0
        findHamiltonianPaths(graph, i)
        res['ejes'].append(i)
        res['prog'].append(prog)
        loading.plusProgress()
    loading.finalize()

    print("\nEscribiendo a csv...")
    df = pd.DataFrame()
    df['x'] = pd.Series(res['ejes'])
    df['n'] = pd.Series(res['prog'])
    df.to_csv(fileName)


analisisHamilton(9, "resultados.csv")

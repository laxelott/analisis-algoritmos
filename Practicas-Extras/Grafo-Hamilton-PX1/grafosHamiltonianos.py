# Una clase para representar un objeto graph
class Graph:

    # Constructor
    def __init__(self, edges, n):

        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]

        # agrega bordes al graph no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def hamiltonianPaths(graph, v, visited, path, n):

    # si se visitan todos los vértices, entonces existe el camino hamiltoniano
    if len(path) == n:
        # imprime el camino hamiltoniano
        print(path)
        return

    # Comprobar si cada arista a partir del vértice `v` conduce a una solución o no
    for w in graph.adjList[v]:

        # procesa solo vértices no visitados como el hamiltoniano
        # La ruta # visita cada vértice exactamente una vez
        if not visited[w]:
            visited[w] = True
            path.append(w)

            # verificar si agregar el vértice `w` a la ruta conduce a la solución o no
            hamiltonianPaths(graph, w, visited, path, n)

            # retractarse
            visited[w] = False
            path.pop()


def findHamiltonianPaths(graph, n):

    # comienza con cada nodo
    for start in range(n):

        # agregar nodo de inicio a la ruta
        path = [start]

        # marcar el nodo de inicio como visitado
        visited = [False] * n
        visited[start] = True

        hamiltonianPaths(graph, start, visited, path, n)


if __name__ == '__main__':

    # considera un grafo completo que tiene 4 vértices
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    # número total de nodos en el graph (etiquetados de 0 a 3)
    n = 4

    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)

    findHamiltonianPaths(graph, n)

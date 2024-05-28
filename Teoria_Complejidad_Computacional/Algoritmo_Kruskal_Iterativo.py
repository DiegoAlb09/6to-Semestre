# Diego Alberto Aranda Gonzalez
# Algoritmo de Kruskal Iterativo

def kruskal():
    #Definimos la función que nos regresa el conjunto al que pertenece un nodo
    def find(i, parent):
        while parent[i] != i:
            i = parent[i]
        return i

    #Definimos la función que une dos conjuntos
    def union(i, j, parent):
        a = find(i, parent)
        b = find(j, parent)
        parent[a] = b

    #Definimos la función principal
    def kruskal_mst(graph):
        parent = []
        for node in range(len(graph)):
            parent.append(node)
        mst = []
        edges = []
        for i in range(len(graph)):
            for j in range(i, len(graph)):
                if graph[i][j] != 0:
                    edges.append((graph[i][j], i, j))
        edges = sorted(edges)
        for edge in edges:
            weight, i, j = edge
            if find(i, parent) != find(j, parent):
                union(i, j, parent)
                mst.append(edge)
        return mst

    #Definimos el grafo de prueba
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]
    print(kruskal_mst(graph))

kruskal()

# Output:
# [(2, 0, 1), (3, 1, 2), (5, 1, 4), (6, 0, 3)]

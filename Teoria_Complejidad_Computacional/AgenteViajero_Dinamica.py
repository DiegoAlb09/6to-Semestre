#Librerias Necesarias
import networkx as nx
import matplotlib.pyplot as plt
import math
import random

#Creamos el grafo
G = nx.Graph()

#Agregamos los nodos
G.add_node("Centro de Distribucion", pos=(21.797002915870696, -102.28046633923687))
G.add_node("Casa 1", pos=(21.85490001683624, -102.26504374226292))
G.add_node("Casa 2", pos=(21.853740600742764, -102.34306832781398))
G.add_node("Casa 3", pos=(21.90351643596852, -102.24558201609902))
G.add_node("Casa 4", pos=(21.90638253550554, -102.28153665890189))
G.add_node("Casa 5", pos=(21.9380714883858, -102.25934916251998))
G.add_node("Casa 6", pos=(21.928195119225208, -102.28013241671694))
G.add_node("Casa 7", pos=(21.886794591014723, -102.28449322733664))

#Funcion de distancia euclidiana
def euclidean_distance(node1, node2):
  x1, y1 = G.nodes[node1]['pos']
  x2, y2 = G.nodes[node2]['pos']
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Creamos la matriz de distancias
distancia_matriz = []
for node1 in G.nodes:
  x1, y1 = G.nodes[node1]['pos']
  distancia_matriz.append([])
  for node2 in G.nodes:
    x2, y2 = G.nodes[node2]['pos']
    distancia_matriz[-1].append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

#Funcion para imprimir la matriz de distancias
def print_matriz(matriz):
  for i in matriz:
    print(i)

def dynamic_programming(matriz):
  n = len(matriz)

  #Crear una tabla para almacenar los resultados de los subproblemas
  dp = [[float('inf')] * n for _ in range(1 << n)]
  dp[1][0] = 0
  #Para rastrear el camino optimo
  parent = [[-1] * n for _ in range(1 << n)]
  #Llenar la tabla dp
  for mask in range(1, 1 << n):
    for u in range(n):
      if mask & (1 << u):
        for v in range(n):
          if mask & (1 << v) and u != v:
            if dp[mask][u] > dp[mask ^ (1 << u)][v] + matriz[v][u]:
              dp[mask][u] = dp[mask ^ (1 << u)][v] + matriz[v][u]
              parent[mask][u] = v

  #Encontrar el camino optimo
  mask = (1 << n) - 1
  last = 0
  min_cost = float('inf')

  for i in range(1, n):
    if min_cost > dp[mask][i] + matriz[i][0]:
      min_cost = dp[mask][i] + matriz[i][0]
      last = i

  path = []
  while last != -1:
    path.append(last)
    next_mask = mask ^ (1 << last)
    next_last = parent[mask][last]
    mask = next_mask
    last = next_last
  
  path.append(0)
  path.reverse()

  return min_cost, path

#Imprimimos el grafo
def graph_plot(matriz, path, cost):
  plt.figure(figsize=(10, 10))
  x = [cost[i][0] for i in path]
  y = [cost[i][1] for i in path]

  plt.plot(x, y, marker='o')
  for i, (xi, yi) in enumerate(cost):
    plt.text(xi, yi, i, fontsize=12, ha='center')

  for i in range(len(path) - 1):
    plt.arrow(cost[path[i]][0], cost[path[i]][1], cost[path[i + 1]][0] - cost[path[i]][0], cost[path[i + 1]][1] - cost[path[i]][1], color='r', length_includes_head=True)

  plt.show()


def main():
  print_matriz(distancia_matriz)
  cost, path = dynamic_programming(distancia_matriz)
  print("Costo minimo: ", cost)
  print("Camino optimo: ", path)
  graph_plot(distancia_matriz, path, [G.nodes[node]['pos'] for node in G.nodes])

if __name__ == "__main__":
  main()
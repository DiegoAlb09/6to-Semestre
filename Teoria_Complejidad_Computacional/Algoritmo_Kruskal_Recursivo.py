# Diego Alberto Aranda Gonzalez
# Algoritmo de Kruskal Recursivo

import numpy as np
import struct
#Definimos el numero maximo de vertices
MAX = 1005
#Union - Find
padre = np.zeros(MAX, dtype=int)

#Método de Inicialización
def MakeSet(n):
  for i in range(n):
    padre[i] = i

#Método para encontrar el padre de un nodo
def Find(u):
  if u == padre[u]:
    return u
  padre[u] = Find(padre[u])
  return padre[u]

#Método para unir dos nodos
def Union(u, v):
  u = Find(u)
  v = Find(v)
  padre[u] = v

#Método que me determina si dos vertices estan en el mismo conjunto
def sameComponent(u, v):
  if Find(u) == Find(v):
    return True
  return False

#Definimos la estructura de una arista, vertice de origen, vertice destino y peso
class Edge:
  def __init__(self, u, v, w):
    self.u = u
    self.v = v
    self.w = w

#Definimos el método de comparación de aristas
def cmp(a, b):
  return a.w - b.w

#Definimos el método principal

def kruskal(edges, n):
  MakeSet(n)
  edges.sort(key=lambda x: x.w)
  mst = []
  for edge in edges:
    if not sameComponent(edge.u, edge.v):
      Union(edge.u, edge.v)
      mst.append(edge)
  return mst

def main():
  n = 6
  m = 3
  edges = []
  edges.append(Edge(0, 1, 2))
  edges.append(Edge(1, 2, 3))
  edges.append(Edge(1, 4, 5))
  mst = kruskal(edges, n)
  print(len(mst))
  for edge in mst:
    print(edge.u, edge.v, edge.w)

if __name__ == "__main__":
  main()

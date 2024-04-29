# Diego Alberto Aranda Gonzalez
# Algortimo de fuerza bruta para resolver el problema del agente viajero
# Universidad Autonoma de Aguascalientes

import itertools
import math

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def distanciaT(camino, ciudades):
    distanciaT = 0
    for i in range(len(camino) - 1):
        distanciaT += distancia(ciudades[camino[i]], ciudades[camino[i + 1]])
    return distanciaT

def agente_viajero_fuerza_bruta(ciudades):
    caminoMcorto = None
    distanciaMcorta = float('inf')
    for camino in itertools.permutations(range(len(ciudades))):
        distancia = distanciaT(camino, ciudades)
        if distancia < distanciaMcorta:
            distanciaMcorta = distancia
            caminoMcorto = camino
    return caminoMcorto, distanciaMcorta

def main():
    ciudades = [(0, 0), (1, 5), (2, 3), (5, 2), (7, 1), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7)]
    caminoMcorto, distanciaMcorta = agente_viajero_fuerza_bruta(ciudades)
    print("El camino más corto es: ", caminoMcorto)
    print("La distancia más corta es: ", distanciaMcorta)
  
main()
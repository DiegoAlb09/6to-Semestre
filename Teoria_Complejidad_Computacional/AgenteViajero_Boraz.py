#Diego Alberto Aranda Gonzalez
#Algoritmo gloton para resolver el problema del agente viajero
#Universidad Autonoma de Aguascalientes

import itertools
import math

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def distanciaT(camino, ciudades):
    distanciaT = 0
    for i in range(len(camino) - 1):
        distanciaT += distancia(ciudades[camino[i]], ciudades[camino[i + 1]])
    return distanciaT

def agente_viajero_greedy(ciudades):
    numCiudades = len(ciudades)
    camino = [0]
    visitadas = set([0])
    for i in range(numCiudades - 1):
        ciudadActual = camino[-1]
        distanciaMinima = float('inf')
        ciudadMasCercana = None
        for siguienteCiudad in range(numCiudades):
            if siguienteCiudad not in visitadas:
                dist = distancia(ciudades[ciudadActual], ciudades[siguienteCiudad])
                if dist < distanciaMinima:
                    distanciaMinima = dist
                    ciudadMasCercana = siguienteCiudad
        camino.append(ciudadMasCercana)
        visitadas.add(ciudadMasCercana)
    camino.append(0)
    return camino

def main():
    ciudades = [(0, 0), (1, 5), (2, 3), (5, 2), (7, 1), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7)]
    camino = agente_viajero_greedy(ciudades)
    print("El camino más corto es: ", camino)
    print("La distancia más corta es: ", distanciaT(camino, ciudades))

main()

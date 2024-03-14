#Algoritmo NP
#Algortimo para minimizar la diferencia entre dos subconjuntos
#Universidad Autonoma de Aguascalientes
#Carrera: Ingenieria en Computacion Inteligente
#Materia: Teoria de la Complejidad Computacional
#Maestra:
#Alumno: Diego Alberto Aranda Gonzalez

# Importamos las librerias
import random
import numpy as np

menor = np.inf
tamañoU = 20
arregloU = []

#Generamos cadenas binarias con el codigo de gray
def gray(tamañoU):
    arregloUG = []
    arregloU = random.sample(range(1, 100), tamañoU)
    #Pasamos el arreglo a binario
    #Pasamos el arreglo a gray
    for i in range(tamañoU):
        arregloUG.append(bin(arregloU[i] ^ (arregloU[i] >> 1))[2:])
    return arregloUG

print("El arreglo U es: ", gray(tamañoU))

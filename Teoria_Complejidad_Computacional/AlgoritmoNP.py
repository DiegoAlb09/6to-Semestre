#Algoritmo NP
#Algortimo para minimizar la diferencia entre dos subconjuntos
#Universidad Autonoma de Aguascalientes
#Carrera: Ingenieria en Computacion Inteligente
#Materia: Teoria de la Complejidad Computacional
#Maestra:
#Alumno: Diego Alberto Aranda Gonzalez

# Importamos las librerias
import numpy as np
import time

n = 20
U = []
# Generamos un arreglo de n elementos
for i in range(n):
   i = np.random.randint(1,100)
   U.append(i)

num = pow(2,n-1)
div = num
g = []
for i in range(n):
    g.append(0)

sumA = 0
sumB = 0
sumT = 0
menor = 100000

combinacion = []

while num != 0:
   numG = num
   divG = div
   print("Numero:", num)
   for m in range(divG):
        if numG % 2 == 1:
             g[m] = 1
        else:
             g[m] = 0
        numG = int(numG / 2)

    

  

#Universidad Autonoma de Aguascalientes
#Carrera: Ingenieria en Computacion Inteligente
#Materia: Teoria de la Complejidad Computacional
#Maestra:
#Alumno: Diego Alberto Aranda Gonzalez

#Pseudocodigo para max (sumatoria a - sumatoria b)

#Librerias
import time
import random

inicio = time.time()

tamañoU = 100

#Generamos el arreglo U con numeros aleatorios
arregloU = []
for i in range(tamañoU):
    i = random.randint(-100, 100)
    arregloU += [i]

#Leemos el arreglo
def leerArreglo(U):
    return U

#Ordenamos el arreglo de menor a mayor con quicksort

def partición(U, primero, ultimo):
    pivote = U[ultimo]
    i = primero - 1

    for j in range(primero, ultimo):
        if U[j] <= pivote:
            i += 1
            (U[i], U[j]) = (U[j], U[i])
    (U[i + 1], U[ultimo]) = (U[ultimo], U[i + 1])
    
    return i + 1

def quicksort(U, primero, ultimo):
    if primero < ultimo:
        pi = partición(U, primero, ultimo)
        quicksort(U, primero, pi - 1)
        quicksort(U, pi + 1, ultimo)

print("El arreglo U es: ", leerArreglo(arregloU))
quicksort(arregloU, 0, len(arregloU) - 1)

#Definimos la suma de A y B
sumaA = 0
sumaB = 0

for i in range (int(len(arregloU)/2)):
  sumaA += arregloU[i]
  sumaB += arregloU[i+int(len(arregloU)/2)]

print("El arreglo ordenado es: ", leerArreglo(arregloU))

#print("La suma de A es: ", sumaA)
#print("La suma de B es: ", sumaB)
print("El maximo es: ", abs(sumaA - sumaB))
print("Se alcanza cuando A contiene a la mitad de los elementos más pequeño de U y B a la mitad de los más grandes, siendo |A|=|B|")
fin = time.time()
print("Tiempo de ejecución: ", fin - inicio)

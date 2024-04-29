#Universidad Autonoma de Aguascalientes
#Ingenieria en Computación Inteligente
#Introducción a los Sistemas Operativos
#Maestra: Clelia Ivette Ruiz Vertiz
#Alumno: Diego Alberto Aranda Gonzalez
#Programa que simula la ejecución de procesos con diferentes algoritmos de planificación
#Tabla de reemplazo de páginas FIFO
#Tabla de reemplazo de páginas Round Robin
import numpy as np
#Menu para seleccionar el algoritmo de planificación
def menu():
  print("-------MENU-------")
  print("1.- FIFO")
  print("2.- Round Robin")
  print("3.- Salir")
  opcion = int(input("Selecciona una opción: "))
  return opcion

#Función principal
def main():
  opcion = menu()
  while opcion != 3:
    if opcion == 1:
      print("Algoritmo FIFO")
      numProcesos = int(input("Ingresa el número de procesos: "))
      #Se crea una matriz para almacenar el orden de llegada y el tiempo de cada proceso
      procesos = np.zeros((numProcesos, 2))
      for i in range(numProcesos):
        procesos[i][0] = int(input("Ingresa el orden de llegada del proceso " + str(i + 1) + ": "))
        procesos[i][1] = int(input("Ingresa el tiempo del proceso " + str(i + 1) + ": "))
      
      #Se ordenan los procesos por orden de llegada
      procesos = procesos[procesos[:,0].argsort()]

      #Se calcula el tiempo de espera y el tiempo de retorno
      tiempoFinalizacion = 0
      tiempoRetorno = 0
      tiempoEsperaTotal = 0
      tiempoRetornoTotal = 0
      tiempoTotal = 0
      tiempoE = 0
      tiempoP = 0
      print("Proceso\tTiempo de llegada\tTiempo de Ejecución\tTiempo de Inicio\tTiempo Finalizacion\tTiempo Total\tTiempo de Espera\tP")
      for i in range(numProcesos):
        tiempoFinalizacion = tiempoRetorno
        tiempoRetorno += procesos[i][1]
        tiempoTotal = tiempoRetorno - procesos[i][0]
        tiempoE = tiempoFinalizacion - procesos[i][0]
        tiempoP = tiempoTotal / procesos[i][1]
        tiempoEsperaTotal += tiempoTotal
        tiempoRetornoTotal += tiempoE
        print(str(i + 1) + "\t" + str(int(procesos[i][0])) + "\t\t\t" + str(int(procesos[i][1])) + "\t\t\t" + str(tiempoFinalizacion) + "\t\t\t" + str(tiempoRetorno) + "\t\t\t" + str(tiempoTotal) + "\t\t\t" + str(tiempoE) + "\t\t\t" + str(tiempoP))
      print("Tiempo Total promedio: ", tiempoEsperaTotal / numProcesos)
      print("Tiempo de retorno promedio: ", tiempoRetornoTotal / numProcesos)
    elif opcion == 2:
      print("Algoritmo Round Robin")
      numProcesos = int(input("Ingresa el número de procesos: "))
      quantum = int(input("Ingresa el quantum: "))
      #Se crea una matriz para almacenar el orden de llegada y el tiempo de cada proceso
      procesos = np.zeros((numProcesos, 2))
      for i in range(numProcesos):
        procesos[i][0] = int(input("Ingresa el orden de llegada del proceso " + str(i + 1) + ": "))
        procesos[i][1] = int(input("Ingresa el tiempo del proceso " + str(i + 1) + ": "))
      
      #Se ordenan los procesos por orden de llegada
      procesos = procesos[procesos[:,0].argsort()]

      #Se calcula el tiempo de espera y el tiempo de retorno
      tiempoInicio = 0
      tiempoRetorno = 0
      tiempoEsperaTotal = 0
      tiempoRetornoTotal = 0
      tiempoTotal = 0
      tiempoE = 0
      tiempoP = 0 
      auxProcesos = np.zeros((numProcesos, 2))
      print("Proceso\tTiempo de llegada\tTiempo de Ejecución\tTiempo de Inicio\tTiempo Finalizacion\tTiempo Total\tTiempo de Espera\tP")

      for i in range(numProcesos):
          #Calculo del tiempo de inicio con el quantum
          tiempoInicio = tiempoRetorno
          auxProcesos[i][1] = procesos[i][1]
          #Si el tiempo de ejecución es mayor al quantum
          if procesos[i][1] > quantum:
            auxProcesos[i][1] -= quantum
            tiempoRetorno += quantum
          else:
            tiempoRetorno += auxProcesos[i][1]
            auxProcesos[i][1] = 0
          print(str(i + 1) + "\t" + str(int(procesos[i][0])) + "\t\t\t" + str(int(procesos[i][1])) + "\t\t\t" + str(tiempoInicio) + "\t\t\t" + str(tiempoRetorno) + "\t\t\t" + str(tiempoTotal) + "\t\t\t" + str(tiempoE) + "\t\t\t" + str(tiempoP))
      #print("Tiempo Total promedio: ", tiempoEsperaTotal / numProcesos)
      #print("Tiempo de retorno promedio: ", tiempoRetornoTotal / numProcesos)
    opcion = menu()

main()




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
def buscarTiempoEspera(procesos,n,bt,wt,quantum):
  rem_bt = [0] * n 
  #Copiamos el tiempo de ejecución de los procesos en rem_bt
  for i in range(n):
    rem_bt[i] = bt[i]
  t = 0

  while(1):
    done = True
    for i in range(n):
      if (rem_bt[i] > 0):
        done = False
        if (rem_bt[i] > quantum):
          t += quantum
          rem_bt[i] -= quantum
        else:
          t = t + rem_bt[i]
          wt[i] = t - bt[i]
          rem_bt[i] = 0
    if (done == True):
      break

def findTurnAroundTime(procesos,n,bt,wt,tat):
  for i in range(n):
    tat[i] = bt[i] + wt[i]

def findavgTime(procesos,n,bt,quantum):
  wt = [0] * n
  tat = [0] * n
  buscarTiempoEspera(procesos,n,bt,wt,quantum)
  findTurnAroundTime(procesos,n,bt,wt,tat)
  total_wt = 0
  total_tat = 0
  print("Proceso\tTiempo de llegada\tTiempo de Ejecución\tTiempo de Espera\tTiempo de Retorno")
  for i in range(n):
    total_wt += wt[i]
    total_tat += tat[i]
    print(str(i + 1) + "\t" + str(int(procesos[i])) + "\t\t\t" + str(int(bt[i])) + "\t\t\t" + str(wt[i]) + "\t\t\t" + str(tat[i]))
  print("Tiempo de espera promedio: ", total_wt / n)
  print("Tiempo de retorno promedio: ", total_tat / n)
  

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
      procesos = np.zeros(numProcesos)
      for i in range(numProcesos):
        procesos[i] = int(input("Ingresa el tiempo de llegada del proceso " + str(i + 1) + ": "))
      tiempoProceso = np.zeros(numProcesos)
      for i in range(numProcesos):
        tiempoProceso[i] = int(input("Ingresa el tiempo del proceso " + str(i + 1) + ": "))
      quantum = int(input("Ingresa el quantum: "))
      findavgTime(procesos,numProcesos,tiempoProceso,quantum)
    opcion = menu()

main()




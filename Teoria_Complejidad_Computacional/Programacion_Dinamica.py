#Programación del problema de la optimización de las varillas
#Con programación dinámica
#Diego Alberto Aranda Gonzalez

#1.- Cuando El Algoritmo es recursivo y no se ha aplicado programacion dinámica
def cortar_varilla(tam_var, lista_p):
    if tam_var == 0:
        return 0
    max_precio = 0
    for i in range(1, tam_var+1):
        valor = lista_p[i] + cortar_varilla(tam_var-i, lista_p)
        if valor > max_precio:
            max_precio = valor
    return max_precio

tam_var = 4
lista_p = [0,1,5,8,9,10,17,17,20,24,30]
print(cortar_varilla(tam_var, lista_p))

#2.- Cuando El Algoritmo es recursivo y se ha aplicado programacion dinámica
def cortar_var(tam_var, lista_p, memory):
    if tam_var == 0:
        return 0
    if memory[tam_var] != -1:
        return memory[tam_var]
    
    mejor_valor = 0
    for i in range(1, tam_var+1):
        valor = lista_p[i] + cortar_var(tam_var-i, lista_p, memory)
        if valor > mejor_valor:
            mejor_valor = valor
    memory[tam_var] = mejor_valor
    return mejor_valor

if __name__ == "__main__":
    lista_p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 4
    memo = [-1] * (n+1)
    print(cortar_var(n, lista_p, memo))

#3.- Cuando El Algoritmo es iterativo y se le ha aplicado programación dinámica
def cortar_varilla_iter(tam_var, lista_p):
  tabla = [0] * (tam_var+1)

  for varilla_actual in range(1,tam_var+1):
      mejor_valor = 0
      for i in range(1, varilla_actual+1):
          valor = lista_p[i] + tabla[varilla_actual-i]
          if valor > mejor_valor:
              mejor_valor = valor

      tabla[varilla_actual] = mejor_valor

  return tabla[tam_var]

if __name__ == "__main__":
    lista_p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 4
    print(cortar_varilla_iter(n, lista_p))

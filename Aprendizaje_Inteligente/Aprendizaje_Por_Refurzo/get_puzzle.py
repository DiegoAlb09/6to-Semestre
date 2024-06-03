#Generamos sudoku de 9x9 y los almacenamos en un .csv

# Importamos las librerias necesarias
import numpy as np
import pandas as pd
import random
import copy

# Sudoku vacio
sudoku = np.zeros((9,9))

# Funcion para imprimir el sudoku
def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = " ")
        print()

# Funcion para verificar si el numero es valido
def is_valid(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False
    return True

# Funcion para resolver el sudoku
def solve_sudoku(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(sudoku, row, col, i):
            sudoku[row][col] = i
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

# Funcion para encontrar la celda vacia
def find_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None


# Generamos un sudoku aleatorio
def generate_sudoku():
    sudoku = np.zeros((9,9), dtype=int)
    solve_sudoku(sudoku)
    for i in range(9):
        for j in range(9):
            if random.random() < 0.5:
                sudoku[i][j] = 0
    return sudoku

# Generamos un sudoku aleatorio
# Almacenamos 10 sudokus en un .csv
for i in range(10):
    sudoku = generate_sudoku()
    df = pd.DataFrame(sudoku)
    df.to_csv('sudoku_{}.csv'.format(i), index=False, header=False)

# Imprimimos el sudoku
print("Sudoku sin resolver:")
print_sudoku(sudoku)
print("\n")
print("Sudoku resuelto:")
solve_sudoku(sudoku)

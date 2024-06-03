# Con el uso de q-learning se resuelve un sudoku

# Importamos las librerias necesarias
import numpy as np

sudoku = []
sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

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

# Imprimimos el sudoku
print("Sudoku sin resolver:")
print_sudoku(sudoku)

# Resolvemos el sudoku
solve_sudoku(sudoku)

# Imprimimos el sudoku resuelto
print("\nSudoku resuelto:")
print_sudoku(sudoku)

#Ahora aplicamos el aprendiza por refuerzo
#Cremos el entorno
class Environment:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudoku_original = [x[:] for x in sudoku]
        self.state = 0
        self.done = False
        self.reward = 0
        self.action_space = [i for i in range(81)]
        self.action_space_size = len(self.action_space)
        self.state_space = [i for i in range(81)]
        self.state_space_size = len(self.state_space)
        self.possible_numbers = [i for i in range(1, 10)]
        self.reset()
        
    def reset(self):
        self.sudoku = [x[:] for x in self.sudoku_original]
        self.state = 0
        self.done = False
        self.reward = 0
        return self.state
    
    def step(self, action, number):
        row = action // 9
        col = action % 9
        if self.sudoku[row][col] == 0:
            self.sudoku[row][col] = number
            if self.is_valid(row, col, number):
                self.state += 1
                if self.state == self.state_space_size:
                    self.done = True
                    self.reward = 1
                else:
                    self.reward = 0
            else:
                self.reward = -1
        else:
            self.reward = -1
        return self.state, self.reward, self.done
    
    def is_valid(self, row, col, number):
        for i in range(9):
            if self.sudoku[row][i] == number or self.sudoku[i][col] == number:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.sudoku[i + start_row][j + start_col] == number:
                    return False
        return True

#Creamos el agente
class Agent:
    def __init__(self, env):
        self.env = env
        self.state = 0
        self.alpha = 0.1
        self.gamma = 0.6
        self.epsilon = 0.1
        self.q_table = np.zeros((self.env.state_space_size, self.env.action_space_size))
        
    def choose_action(self):
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice(self.env.action_space)
        else:
            action = np.argmax(self.q_table[self.state])
        return action
    
    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.gamma * np.max(self.q_table[next_state])
        self.q_table[state, action] = self.q_table[state, action] + self.alpha * (target - predict)
        
    def train(self, episodes):
        for episode in range(episodes):
            self.state = self.env.reset()
            done = False
            while not done:
                action = self.choose_action()
                number = np.random.choice(self.env.possible_numbers)
                next_state, reward, done = self.env.step(action, number)
                self.learn(self.state, action, reward, next_state)
                self.state = next_state
        print("Training finished.")
        
    def test(self):
        self.state = self.env.reset()
        done = False
        while not done:
            action = np.argmax(self.q_table[self.state])
            number = np.random.choice(self.env.possible_numbers)
            next_state, reward, done = self.env.step(action, number)
            self.state = next_state
        print("Testing finished.")

#Creamos el entorno y el agente
env = Environment(sudoku)
agent = Agent(env)

#Entrenamos el agente
agent.train(5)

#Probamos el agente
agent.test()

#Imprimimos el sudoku resuelto por el agente
print("\nSudoku resuelto por el agente:")
print_sudoku(env.sudoku)

#Imprimimos la tabla Q
print("\nQ-table:")
print(agent.q_table)

#Imprimimos la politica optima
print("\nOptimal policy:")
optimal_policy = np.argmax(agent.q_table, axis = 1)
optimal_policy = np.reshape(optimal_policy, (9, 9))
print(optimal_policy)

#Imprimimos la politica optima en el sudoku
print("\nOptimal policy in the sudoku:")
sudoku_policy = [x[:] for x in sudoku]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            sudoku_policy[i][j] = optimal_policy[i][j]

print_sudoku(sudoku_policy)

#Imprimimos la politica optima en el sudoku original
print("\nOptimal policy in the original sudoku:")
sudoku_policy_original = [x[:] for x in sudoku]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            sudoku_policy_original[i][j] = optimal_policy[i][j]

print_sudoku(sudoku_policy_original)

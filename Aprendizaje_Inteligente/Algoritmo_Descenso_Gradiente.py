# Algoritmo de descenso de gradiente para minimizar una función de costo

# Importar librerias
import numpy as np
import matplotlib.pyplot as plt

# Funcion
def f(x):
    return 2*x**2 * np.cos(x) - 5*x

# Derivada de la funcion
def df(x):
    return 4*x*np.cos(x) - 2*x**2*np.sin(x) - 5

# Definimos el rango de la grafica
x = np.linspace(-5, 5, 100)
y = f(x)

# Graficamos la funcion
plt.plot(x, y, label='f(x) = 2x^2 * cos(x) - 5x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()



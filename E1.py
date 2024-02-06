#Universidad Autonoma de Aguascalientes
#Departamento de Ciencias de la Computacion 
#Carrera de Ingenieria en Computacion Inteligente
#Materia Aprendizaje Inteligente
#Maestro Dr. Francisco Javier Luna Rosas
#Alumno: Diego Alberto Aranda Gonzalez
#Semestre Ene-Junio 2024

#Neuron MacCulloch-Pitts
#Determinar si se le aprueba o no una tarjeta de credito a un cliente considerando 
#la edad y el ahorro que tiene en su cuenta bancaria

#Librerias
import numpy as np
import matplotlib.pyplot as plt

#Datos de 10 personas -> Edad y Ahorro

personas = np.array([[0.3,0.4],[0.4,0.3],
                     [0.3,0.2],[0.4,0.1],
                     [0.5,0.4],[0.4,0.8],
                     [0.6,0.6],[0.5,0.6],
                     [0.7,0.6],[0.8,0.5]
                     ])

clases = np.array([0,0,0,0,0,1,1,1,1,1])
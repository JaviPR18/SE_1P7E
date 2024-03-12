
"""
Created on Sun Mar 10 20:11:15 2024

@author: javip
"""

import numpy as np

# Definir la matriz de transición de actividades diarias
# En este ejemplo, tenemos 3 actividades: estudiar (A), deportes (B), descansar (C)
# La matriz de transición representa las probabilidades de cambiar de una actividad a otra.
matriz_transicion = np.array([[0.6, 0.2, 0.2],
                              [0.3, 0.5, 0.2],
                              [0.1, 0.3, 0.6]])

# Definir la actividad inicial
# En este ejemplo, comenzamos con estudiar (A)
actividad_inicial = 0

# Simulación de la elección de actividades diarias
num_dias = 7  # Simulamos una semana (7 días)
actividad_actual = actividad_inicial

print("Secuencia de actividades diarias:")
for _ in range(num_dias):
    print(["Estudiar", "Deportes", "Descansar"][actividad_actual], end=" ")
    # Escoge la próxima actividad con base en la matriz de transición
    actividad_actual = np.random.choice([0, 1, 2], p=matriz_transicion[actividad_actual])

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:07:45 2024

@author: javip
"""

import numpy as np

# Número de rutas disponibles
num_rutas = 4

# Velocidad verdadera promedio para cada ruta (puede ser desconocida en la práctica)
velocidades_verdaderas = np.random.normal(0, 1, num_rutas)

# Inicialización de la velocidad estimada promedio y recuento de selección de rutas
velocidad_estimada = np.zeros(num_rutas)
contador_seleccion = np.zeros(num_rutas)

# Número total de días (iteraciones)
num_dias = 1000

# Parámetro epsilon para equilibrar exploración y explotación
epsilon = 0.1

# Historial de velocidades obtenidas
velocidades_historial = []

for dia in range(num_dias):
    if np.random.random() < epsilon:
        # Exploración: elige una ruta al azar
        ruta_elegida = np.random.choice(num_rutas)
    else:
        # Explotación: elige la ruta con la velocidad estimada más alta
        ruta_elegida = np.argmax(velocidad_estimada)

    # Simular la velocidad para la ruta elegida
    velocidad = np.random.normal(velocidades_verdaderas[ruta_elegida], 1)
    
    # Actualizar la velocidad estimada y el contador de selección de la ruta
    contador_seleccion[ruta_elegida] += 1
    velocidad_estimada[ruta_elegida] += (velocidad - velocidad_estimada[ruta_elegida]) / contador_seleccion[ruta_elegida]

    # Registrar la velocidad obtenida en el historial
    velocidades_historial.append(velocidad)

# Calcular la velocidad total acumulada
velocidad_total = sum(velocidades_historial)

print(f"Velocidad total acumulada: {velocidad_total}")

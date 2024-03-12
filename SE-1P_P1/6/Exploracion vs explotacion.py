import numpy as np

# Velocidades verdaderas promedio para cada ruta (datos específicos)
velocidades_verdaderas = [60, 50, 45, 50]

# Inicialización de la velocidad estimada promedio y recuento de selección de rutas
velocidad_estimada = [0] * len(velocidades_verdaderas)
contador_seleccion = [0] * len(velocidades_verdaderas)

# Número total de días (iteraciones)
num_dias = 365

# Parámetro epsilon para equilibrar exploración y explotación
epsilon = 0.2

# Historial de velocidades obtenidas
velocidades_historial = []

for dia in range(num_dias):
    if np.random.random() < epsilon:
        # Exploración: elige una ruta al azar
        ruta_elegida = np.random.choice(len(velocidades_verdaderas))
    else:
        # Explotación: elige la ruta con la velocidad estimada más alta
        ruta_elegida = np.argmax(velocidad_estimada)

    # Simular la velocidad para la ruta elegida (en este caso, se usa la velocidad verdadera)
    velocidad = velocidades_verdaderas[ruta_elegida]
    
    # Actualizar la velocidad estimada y el contador de selección de la ruta
    contador_seleccion[ruta_elegida] += 1
    velocidad_estimada[ruta_elegida] += (velocidad - velocidad_estimada[ruta_elegida]) / contador_seleccion[ruta_elegida]

    # Registrar la velocidad obtenida en el historial
    velocidades_historial.append(velocidad)

# Calcular la velocidad total acumulada
velocidad_total = sum(velocidades_historial)

print(f"Velocidad total acumulada: {velocidad_total}")

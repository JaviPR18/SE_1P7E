# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:45:38 2024

@author: javip
"""

import math
import random

def funcion_objetivo(temperatura):
    # La función objetivo representa el sabor del té.
    # Queremos maximizar el sabor, y asumimos que hay una temperatura ideal para eso.
    temperatura_ideal = 70  # Temperatura ideal para preparar el té
    return -abs(temperatura - temperatura_ideal)**2 + 50

def temple_simulado(funcion_objetivo, temperatura_inicial, tasa_enfriamiento, iteraciones):
    mejor_temperatura = random.uniform(0, 100)  # Genera una temperatura inicial aleatoria
    mejor_valor = funcion_objetivo(mejor_temperatura)
    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones):
        nueva_temperatura = mejor_temperatura + random.uniform(-5, 5)  # Genera una temperatura vecina aleatoria
        valor_nueva_temperatura = funcion_objetivo(nueva_temperatura)

        # Comprueba si la nueva temperatura es mejor o si se acepta con una cierta probabilidad
        if valor_nueva_temperatura > mejor_valor or random.random() < math.exp((valor_nueva_temperatura - mejor_valor) / temperatura_actual):
            mejor_temperatura = nueva_temperatura
            mejor_valor = valor_nueva_temperatura

        # Enfría la temperatura
        temperatura_actual *= tasa_enfriamiento

    return mejor_temperatura, mejor_valor

if __name__ == "__main__":
    temperatura_inicial = 80.0
    tasa_enfriamiento = 0.95
    iteraciones = 1000

    mejor_temperatura, mejor_valor = temple_simulado(funcion_objetivo, temperatura_inicial, tasa_enfriamiento, iteraciones)

    print(f"Mejor temperatura encontrada para preparar el té: {mejor_temperatura}°C, Valor = {mejor_valor}")

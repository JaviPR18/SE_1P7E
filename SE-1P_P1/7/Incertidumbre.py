# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:59:44 2024

@author: javip
"""

import math

# Gastos mensuales en diversas categorías
gastos_mensuales = [5000, 1200, 5000, 1300, 5100, 1050, 250]

# Calcular la media (promedio) de los gastos mensuales
mean = sum(gastos_mensuales) / len(gastos_mensuales)

# Calcular la suma de los cuadrados de las diferencias entre cada gasto y la media
sum_of_squared_differences = sum((x - mean) ** 2 for x in gastos_mensuales)

# Calcular la varianza (promedio de los cuadrados de las diferencias)
variance = sum_of_squared_differences / len(gastos_mensuales)

# Calcular la desviación estándar (raíz cuadrada de la varianza)
std_deviation = math.sqrt(variance)

# Imprimir la desviación estándar
print("Desviación estándar de gastos mensuales:", std_deviation)

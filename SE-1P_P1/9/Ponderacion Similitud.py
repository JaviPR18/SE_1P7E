# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:12:32 2024

@author: javip
"""

import random

# Función de densidad de probabilidad para el consumo de gasolina
def pdf_consumo_gasolina(x):
    # Supongamos una distribución triangular centrada en 10 litros/100 km
    punto_pico = 10
    if x <= punto_pico:
        return (2 / punto_pico**2) * x
    else:
        return (2 / punto_pico**2) * (2*punto_pico - x)

# Función para realizar muestreo por rechazo
def muestreo_por_rechazo_consumo_gasolina(pdf, x_min, x_max):
    while True:
        x = random.uniform(x_min, x_max)
        y = random.uniform(0, pdf(x_max))
        
        if y <= pdf(x):
            return x

# Definir los límites para el consumo de gasolina (en litros/100 km)
consumo_minimo = 5
consumo_maximo = 20

# Realizar muestreo por rechazo para simular el consumo de gasolina
muestra_consumo_gasolina = muestreo_por_rechazo_consumo_gasolina(pdf_consumo_gasolina, consumo_minimo, consumo_maximo)
print("Consumo de gasolina simulado:", muestra_consumo_gasolina, "litros/100 km")

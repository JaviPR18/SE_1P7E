# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:03:37 2024

@author: javip
"""

import random

# Definir las categorías de actividades
CATEGORIAS = {
    0: "Trabajo",
    1: "Ejercicio",
    2: "Tiempo con la familia",
    3: "Tiempo con amigos",
    4: "Relajación",
    5: "Novia",
    6: "Retas",
 
}

def estado_inicial(n_actividades):
    return [random.randint(0, 6) for _ in range(n_actividades)]  # Representamos la semana con 7 días

def num_conflictos(estado, indice_actividad):
    conflictos = 0
    for i in range(len(estado)):
        if i == indice_actividad:
            continue
        if estado[i] == estado[indice_actividad]:
            conflictos += 1
    return conflictos

def minimos_conflictos(csp, max_pasos=1000):
    estado = estado_inicial(len(csp))
    for _ in range(max_pasos):
        actividades_en_conflicto = [i for i in range(len(csp)) if num_conflictos(estado, i) > 0]
        if not actividades_en_conflicto:
            return estado
        actividad_a_mover = random.choice(actividades_en_conflicto)
        dia_conflicto_minimo = random.choice([d for d in range(7) if d != estado[actividad_a_mover]])
        estado[actividad_a_mover] = dia_conflicto_minimo
    return None

def imprimir_horario(estado):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for actividad, dia in enumerate(estado):
        print(f"{dias_semana[dia]}: {CATEGORIAS[actividad]}")

if __name__ == "__main__":
    n = len(CATEGORIAS)  # Número de categorías de actividades
    solucion = minimos_conflictos(range(n))
    if solucion:
        print("Horario encontrado:")
        imprimir_horario(solucion)
    else:
        print("No se encontró un horario sin conflictos después de un número máximo de iteraciones.")


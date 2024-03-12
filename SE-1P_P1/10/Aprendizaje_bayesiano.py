# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:37:27 2024

@author: javip
"""

import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# Crear un conjunto de datos ficticio sobre comentarios de la compra de autos chinos
# Puedes reemplazar esto con tu propio conjunto de datos
datos = [
    ("Compré un auto chino y estoy muy satisfecho con el rendimiento", "positivo"),
    ("No recomendaría comprar un auto chino, tuve muchos problemas", "negativo"),
    ("La relación calidad-precio de los autos chinos es excelente", "positivo"),
    ("El servicio al cliente del concesionario de autos chinos es deficiente", "negativo"),
    # Agrega más ejemplos según sea necesario
]

# Define una función para extraer características de un comentario sobre la compra de un auto chino
def caracteristicas_documento(documento):
    palabras = set(documento)
    caracteristicas = {}
    for palabra in palabras:
        caracteristicas['contiene(%s)' % palabra] = (palabra in palabras)
    return caracteristicas

# Obtén las palabras más frecuentes en los comentarios de la compra de autos chinos
todas_palabras = nltk.FreqDist(palabra.lower() for (texto, _) in datos for palabra in nltk.word_tokenize(texto))
caracteristicas_palabras = list(todas_palabras.keys())[:200]

# Crea conjuntos de entrenamiento y prueba
conjunto_caracteristicas = [(caracteristicas_documento(texto.split()), etiqueta) for (texto, etiqueta) in datos]
conjunto_entrenamiento, conjunto_prueba = conjunto_caracteristicas[:int(len(conjunto_caracteristicas) * 0.8)], conjunto_caracteristicas[int(len(conjunto_caracteristicas) * 0.8):]

# Entrena un clasificador de Bayes ingenuo
clasificador = NaiveBayesClassifier.train(conjunto_entrenamiento)

# Evalúa el clasificador
print("Exactitud del clasificador:", accuracy(clasificador, conjunto_prueba))

# Ejemplo de clasificación
texto_a_clasificar = "Estoy considerando comprar un auto chino, ¿alguna recomendación?"
caracteristicas_texto = caracteristicas_documento(texto_a_clasificar.split())
resultado = clasificador.classify(caracteristicas_texto)
print("Clasificación:", resultado)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:25:25 2024

@author: javip
"""

import os
import json

class ChatBot:
    def __init__(self):
        self.base_datos_path = 'base_datos.json'
        self.base_datos = self.cargar_base_datos()

    def cargar_base_datos(self):
        if os.path.exists(self.base_datos_path):
            with open(self.base_datos_path, 'r') as file:
                base_datos = json.load(file)
            return base_datos
        else:
            return {'hola': '¡Hola! ¿En qué puedo ayudarte hoy?',
                    'como estas': 'Estoy bien, gracias. ¿Y tú?',
                    'de que quieres hablar': 'Podemos hablar de cualquier cosa. ¿Tienes algún tema en mente?'}

    def guardar_base_datos(self):
        with open(self.base_datos_path, 'w') as file:
            json.dump(self.base_datos, file)

    def procesar_pregunta(self, pregunta):
        respuesta = self.base_datos.get(pregunta, None)
        if respuesta is not None:
            return respuesta
        else:
            nuevo_conocimiento = input(f"No encontré una respuesta para '{pregunta}'. ¿Puedes proporcionar información para agregar a la base de datos? ")
            self.actualizar_base_datos(pregunta, nuevo_conocimiento)
            return f"¡Gracias por la información sobre '{pregunta}'! Ahora puedo responder mejor."

    def actualizar_base_datos(self, pregunta, respuesta):
        self.base_datos[pregunta] = respuesta
        self.guardar_base_datos()

# Crear una instancia del chatbot
chatbot = ChatBot()

# Ejemplo de interacción
while True:
    input_usuario = input("Usuario: ")
    if input_usuario.lower() == 'salir':
        break
    respuesta_chatbot = chatbot.procesar_pregunta(input_usuario)
    print(f"ChatBot: {respuesta_chatbot}")

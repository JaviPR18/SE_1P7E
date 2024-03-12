def busqueda_bidireccional(grafo, inicio, objetivo):
    cola_adelante = [inicio]
    cola_atras = [objetivo]
    visitados_adelante = {inicio}
    visitados_atras = {objetivo}

    while cola_adelante and cola_atras:
        # Expandir desde la dirección adelante
        nodo_actual = cola_adelante.pop(0)
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados_adelante:
                visitados_adelante.add(vecino)
                cola_adelante.append(vecino)
            if vecino in visitados_atras:
                return vecino  # Se encontró un nodo de conexión

        # Expandir desde la dirección atrás
        nodo_actual = cola_atras.pop(0)
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados_atras:
                visitados_atras.add(vecino)
                cola_atras.append(vecino)
            if vecino in visitados_adelante:
                return vecino  # Se encontró un nodo de conexión

    return None  # No se encontró un camino entre los nodos

# Ejemplo de un grafo representado como un diccionario de adyacencia
grafo = {
    'Casa': ['Av.Patria', 'Alcalde'],
    'Av.Patria': ['Trabajo','ceti'],
    'Alcalde': ['Trabajo'],
    'Trabajo': ['Alcalde'],
    'Ceti': ['Av.Patria'],
}

nodo_inicio = 'Casa'
nodo_objetivo = 'Ceti'

print("Búsqueda Bidireccional:")
resultado = busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo)

if resultado is not None:
    print(f"Se encontró un camino de {nodo_inicio} a {nodo_objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {nodo_inicio} a {nodo_objetivo}.")


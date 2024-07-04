import heapq

def dijkstra(grafo, inicio, fin):
    # Crear una cola de prioridad
    cola = []
    # Agregar el nodo de inicio con distancia 0
    heapq.heappush(cola, (0, inicio))
    # Diccionario para almacenar la distancia más corta a cada nodo
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    # Diccionario para almacenar el camino más corto
    camino_mas_corto = {nodo: None for nodo in grafo}

    while cola:
        # Obtener el nodo con la distancia más pequeña
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si la distancia más pequeña es mayor que la distancia conocida, omitir el nodo
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Revisar todos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Considerar este nuevo camino solo si es mejor
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino_mas_corto[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))

    # Para reconstruir el camino más corto
    camino = []
    while fin is not None:
        camino.append(fin)
        fin = camino_mas_corto[fin]
    camino = camino[::-1]  # Invertir el camino

    return camino, distancias[camino[-1]]

# Definir el grafo como un diccionario
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Encontrar el camino más corto de A a E
camino_mas_corto, distancia = dijkstra(grafo, 'A', 'E')
print("Camino más corto:", camino_mas_corto)
print("Distancia:", distancia)

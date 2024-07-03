from collections import deque

def bfs(grafo, nodo_inicio):
    # Cola para almacenar los nodos por visitar
    cola = deque([nodo_inicio])
    # Conjunto para mantener registro de nodos visitados
    visitados = set([nodo_inicio])

    while cola:
        nodo_actual = cola.popleft()
        print(nodo_actual, end=' ')

        # Recorrer todos los nodos adyacentes del nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Realizar BFS comenzando desde el nodo 'A'
print("Recorrido BFS:")
bfs(grafo, 'A')

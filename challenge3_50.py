def dfs(grafo, nodo, visitados):
    # Marcar el nodo actual como visitado
    visitados.add(nodo)
    print(nodo, end=' ')

    # Recorrer todos los nodos adyacentes no visitados
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Conjunto para mantener registro de nodos visitados
visitados = set()

# Realizar DFS desde cada nodo no visitado
print("Recorrido DFS:")
for nodo in grafo:
    if nodo not in visitados:
        dfs(grafo, nodo, visitados)


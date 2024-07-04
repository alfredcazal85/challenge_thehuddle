class ColaDePrioridad:
    def __init__(self):
        self.cola = []

    def insertar(self, elemento, prioridad):
        # Insertar el elemento con su prioridad en la cola
        self.cola.append((prioridad, elemento))
        # Ordenar la cola por prioridad (menor prioridad primero)
        self.cola.sort(key=lambda x: x[0])

    def eliminar(self):
        if self.esta_vacia():
            return None
        # Eliminar y retornar el elemento con la mayor prioridad (menor valor numérico)
        return self.cola.pop(0)[1]

    def esta_vacia(self):
        return len(self.cola) == 0

    def __str__(self):
        return str(self.cola)

# Crear la cola de prioridad
cola_prioridad = ColaDePrioridad()

# Insertar 5 elementos con diferentes prioridades
elementos_con_prioridad = [(10, 'Elemento1'), (5, 'Elemento2'), (15, 'Elemento3'), (1, 'Elemento4'), (20, 'Elemento5')]

for prioridad, elemento in elementos_con_prioridad:
    cola_prioridad.insertar(elemento, prioridad)

print("Cola de prioridad después de insertar los elementos:")
print(cola_prioridad)

# Eliminar elementos de la cola de prioridad
print("Eliminando elementos de la cola de prioridad:")
for _ in range(5):
    elemento_eliminado = cola_prioridad.eliminar()
    print(f"Elemento eliminado: {elemento_eliminado}")

print("Cola de prioridad después de eliminar todos los elementos:")
print(cola_prioridad)

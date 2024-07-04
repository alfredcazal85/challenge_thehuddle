class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def frente(self):
        if self.esta_vacia():
            return None
        return self.cola[0]

    def __str__(self):
        return str(self.cola)

# Crear una cola e insertar 5 elementos
cola = Cola()
elementos = [1, 2, 3, 4, 5]

for elemento in elementos:
    cola.encolar(elemento)

print("Cola después de encolar los elementos:")
print(cola)

# Desencolar elementos de la cola
print("Desencolando elementos de la cola:")
for _ in range(5):
    elemento_desencolado = cola.desencolar()
    print(f"Elemento desencolado: {elemento_desencolado}")

print("Cola después de desencolar todos los elementos:")
print(cola)


class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.pila.pop()

    def esta_vacia(self):
        return len(self.pila) == 0

    def cima(self):
        if self.esta_vacia():
            return None
        return self.pila[-1]

    def __str__(self):
        return str(self.pila)

# Crear una pila e insertar 5 elementos
pila = Pila()
elementos = [1, 2, 3, 4, 5]

for elemento in elementos:
    pila.apilar(elemento)

print("Pila después de apilar los elementos:")
print(pila)

# Desapilar elementos de la pila
print("Desapilando elementos de la pila:")
for _ in range(5):
    elemento_desapilado = pila.desapilar()
    print(f"Elemento desapilado: {elemento_desapilado}")

print("Pila después de desapilar todos los elementos:")
print(pila)

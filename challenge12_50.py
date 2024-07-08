class Figura:
    def imprimir(self):
        print("Esto es una figura.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Esto es un círculo con radio: {self.radio}")

# Ejemplo de uso:
figura = Figura()
figura.imprimir()  # Output: Esto es una figura.

circulo = Circulo(5)
circulo.imprimir()  # Output: Esto es un círculo con radio: 5

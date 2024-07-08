import math

class FormaGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio * self.radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo de uso:
rectangulo = Rectangulo(3, 4)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")  # Output: Área del rectángulo: 12
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")  # Output: Perímetro del rectángulo: 14

circulo = Circulo(5)
print(f"Área del círculo: {circulo.calcular_area()}")  # Output: Área del círculo: 78.53981633974483
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")  # Output: Perímetro del círculo: 31.41592653589793

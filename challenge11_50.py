class Punto2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f'Coordenadas: ({self.x}, {self.y})')

# Ejemplo de uso:
punto = Punto2D(3, 4)
punto.imprimir_coordenadas()  # Output: Coordenadas: (3, 4)

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        return f"Motor {self.tipo} con una potencia de {self.potencia} HP"

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        return f"Auto {self.marca} {self.modelo} con {self.motor.describir()}"

# Ejemplo de uso:
motor = Motor("V8", 450)
auto = Auto("Ford", "Mustang", motor)
print(auto.describir_auto())  # Output: Auto Ford Mustang con Motor V8 con una potencia de 450 HP

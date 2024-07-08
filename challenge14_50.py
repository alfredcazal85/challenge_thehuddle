class Animal:
    def hacerSonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacerSonido(self):
        print("El perro ladra: ¡Guau!")

# Ejemplo de uso:
animal = Animal()
animal.hacerSonido()  # Output: El animal hace un sonido.

perro = Perro()
perro.hacerSonido()  # Output: El perro ladra: ¡Guau!

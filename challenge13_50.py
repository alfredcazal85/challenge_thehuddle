class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad} unidades. Nuevo saldo: {self.saldo} unidades.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def consultar_saldo(self):
        print(f"Tu saldo actual es: {self.saldo} unidades.")
        return self.saldo

# Ejemplo de uso:
cuenta = CuentaBancaria(100)  # Inicializa la cuenta con un saldo de 100 unidades.
cuenta.consultar_saldo()      # Output: Tu saldo actual es: 100 unidades.
cuenta.depositar(50)          # Output: Has depositado 50 unidades. Nuevo saldo: 150 unidades.
cuenta.consultar_saldo()      # Output: Tu saldo actual es: 150 unidades.
cuenta.depositar(20)         # Output: La cantidad a depositar debe ser positiva.

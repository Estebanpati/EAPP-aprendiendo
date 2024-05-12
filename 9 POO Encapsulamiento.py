#ATRIBUTOS PRIVADOS
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo

# Crear una cuenta bancaria
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Intentar acceder al atributo privado (no recomendado)
# print(mi_cuenta.__saldo)  # Error: AttributeError

# Acceder al saldo utilizando un método público
print(f"Saldo actual: ${mi_cuenta.obtener_saldo()}")

# Realizar una transacción
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)

# Verificar el saldo actual
print(f"Saldo actual después de transacciones: ${mi_cuenta.obtener_saldo()}")

class Banco:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.cuentas = []  # Lista de cuentas bancarias

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def consultar_saldo(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero == numero_cuenta:
                print(f"Saldo de la cuenta {numero_cuenta}: ${cuenta.saldo}")
                return
        print(f"No se encontró la cuenta {numero_cuenta}.")

class CuentaBancaria:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

# Uso:
banco = Banco("Mi Banco", "Ciudad X")
cuenta1 = CuentaBancaria("12345", 1000)
cuenta2 = CuentaBancaria("67890", 500)
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)
banco.consultar_saldo("12345")

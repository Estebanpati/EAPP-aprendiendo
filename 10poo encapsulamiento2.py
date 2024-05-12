class Registro:
    def __init__(self):
        self.__entradas = []

    def __validar_entrada(self, entrada):
        if len(entrada) > 5:
            return True
        else:
            return False

    def agregar_entrada(self, nueva_entrada):
        if self.__validar_entrada(nueva_entrada):
            self.__entradas.append(nueva_entrada)
            print("Entrada agregada correctamente")
        else:
            print("La entrada no cumple con los requisitos")

    def obtener_entradas(self):
        return self.__entradas

# Crear un registro
mi_registro = Registro()

# Agregar entradas (una válida y otra inválida)
mi_registro.agregar_entrada("Registro válido")
mi_registro.agregar_entrada("No válido")

# Obtener las entradas
print("Entradas registradas:")
for entrada in mi_registro.obtener_entradas():
    print(entrada)
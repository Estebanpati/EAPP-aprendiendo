class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def calcular_bono(self, porcentaje):
        bono = self.salario * (porcentaje / 100)
        return bono

    def actualizar_salario(self, aumento):
        self.salario += aumento

# Uso:
empleado1 = Empleado("Ana", "Desarrollador", 50000)
print(f"{empleado1.nombre} tiene un salario de ${empleado1.salario}")

empleado1.actualizar_salario(3000)
print(f"Después del aumento, el nuevo salario es ${empleado1.salario}")
print(f"Bono anual: ${empleado1.calcular_bono(10)}")

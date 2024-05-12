class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Trabajador:
    def __init__(self, salario):
        self.salario = salario

class Empleado(Persona, Trabajador):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        Trabajador.__init__(self, salario)

# Crear un objeto de la clase Empleado
mi_empleado = Empleado("Juan", 50000)
print(f"Nombre del empleado: {mi_empleado.nombre}")  # Resultado: "Juan"
print(f"Salario del empleado: {mi_empleado.salario}")  # Resultado: 50000

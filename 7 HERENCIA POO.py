"""HERENCIA SIMPLE"""
class Vehiculo:
    def __init__(self, marca):
        self.marcaa = marca

class Coche(Vehiculo):
    def conducir(self):
        return f"Conduciendo el coche de marca {self.marcaa}"

mi_coche = Coche('TOYOTA')
print(mi_coche.conducir())


"""HERENCIA MULTIPLE"""
class Animal:
    def sonido(self):
        pass
class Volador:
    def volar(self):
        return "Volando alto"
class Pajaro(Animal, Volador):
    def __init__(self, nombre):
        self.nombree = nombre
    def sonido(self):
        return "Pio Pio"

mi_pajaro = Pajaro("Canario")
print(f"Nombre del pajaro: {mi_pajaro.nombree}")
print(f"Sonido del pajaro: {mi_pajaro.sonido()}")
print(f"¿Puedo volar? {mi_pajaro.volar()}")




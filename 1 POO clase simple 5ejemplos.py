
class Persona:
    def __init__(self, nombregg, edadgg):
        self.nombre = nombregg
        self.edad = edadgg
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
# Crear un objeto de la clase Persona
juan = Persona("Juan", 30)
# Invocacion al metodo saludar dentro el objeto juan
juan.saludar()


class Coche:
    def __init__(self, marcahh, modelohh):
        self.marca = marcahh
        self.modelo = modelohh
    def describir(self):
        print(f"Este coche es un {self.marca} {self.modelo}.")
# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
# invocacion al metodo describir dentro el objeto mi_coche
mi_coche.describir()

class Libro:
    def __init__(self, titulott, autortt):
        self.titulo = titulott
        self.autor = autortt
    def detalles(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}")
# Crear un objeto de la clase Libro
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez")
# invocacion al metodo detalles dentro el objeto mi_libro
mi_libro.detalles()


class Rectangulo:
    def __init__(self, b, a):
        self.base = b
        self.altura = a
    def calcular_area(self):
        return self.base * self.altura
# Crear un objeto de la clase Rectángulo
mi_rectangulo = Rectangulo(5, 3)
# invocacion al metodo calcular_area(), dentro el objeto mi_rectangulo
print(f"Área del rectángulo: {mi_rectangulo.calcular_area()}")


class Perro:
    def __init__(self, nnombre, rraza):
        self.nombre = nnombre
        self.raza = rraza
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")
# Crear un objeto de la clase Perro
mi_perro = Perro("Max", "Labrador")
# invocacion del metodo ladrar dentro el objeto mi_perro
mi_perro.ladrar()

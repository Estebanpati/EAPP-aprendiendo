#Polimorfismo con Clases y Métodos:

class Figura:
    def calcular_area(self):
        pass
#Luego, creamos dos clases derivadas: Rectangulo y Circulo. Cada una de ellas implementa
# el método calcular_area() de forma diferente:
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.14 * self.radio ** 2

#Creamos objetos de ambas clases y llamamos al método calcular_area():
rectangulo = Rectangulo(base=5, altura=3)
circulo = Circulo(radio=2)

print(f"Área del rectángulo: {rectangulo.calcular_area()}")  # Resultado: 15
print(f"Área del círculo: {circulo.calcular_area()}")          # Resultado: 12.56

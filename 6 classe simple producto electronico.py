
class ProductoElectrónico:
    def __init__(self, nombre, precio, marca, especificaciones):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.especificaciones = especificaciones

    def mostrar_detalles(self):
        print(f"{self.marca} {self.nombre}: ${self.precio}")
        print(f"Especificaciones: {self.especificaciones}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

# Uso:
telefono = ProductoElectrónico("Teléfono", 500, "Samsung", "Pantalla AMOLED, 128 GB")
telefono.mostrar_detalles()
telefono.actualizar_precio(450)
print(f"Nuevo precio: ${telefono.precio}")

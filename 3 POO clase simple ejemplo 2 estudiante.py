
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def calcular_promedio(self):
        if not self.materias:
            return 0
        total_notas = sum(materia.nota for materia in self.materias)
        return total_notas / len(self.materias)

class Materia:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# Uso:
estudiante = Estudiante("Ana", 20)
materia1 = Materia("Matemáticas", 85)
materia2 = Materia("Historia", 70)
estudiante.agregar_materia(materia1)
estudiante.agregar_materia(materia2)
print(f"Promedio de {estudiante.nombre}: {estudiante.calcular_promedio()}")


"""¡Claro! Vamos a analizar el **método `calcular_promedio`** en detalle:

1. **Definición del Método**:
    - `def calcular_promedio(self):`: Este método se encuentra dentro de la clase "Estudiante". Es una función que calcula el promedio de notas del estudiante en todas sus materias.

2. **Verificación de Materias**:
    - `if not self.materias:`: Esta línea verifica si la lista de materias (`self.materias`) está vacía.
    - Si no hay materias registradas para el estudiante (la lista está vacía), el método retorna directamente un promedio de 0.

3. **Cálculo del Total de Notas**:
    - `total_notas = sum(materia.nota for materia in self.materias)`: Aquí utilizamos una **comprensión de listas** para sumar todas las notas de las materias.
    - `materia.nota` representa la nota de cada materia en la lista.

4. **Cálculo del Promedio**:
    - `return total_notas / len(self.materias)`: Calculamos el promedio dividiendo la suma total de notas entre la cantidad de materias.
    - `len(self.materias)` nos da el número de materias registradas.

En resumen, el método `calcular_promedio` verifica si hay materias, suma las notas y calcula el promedio. Si no hay materias, devuelve 0. Este método es útil para obtener el rendimiento académico promedio del estudiante. 📚🎓"""

#Polimorfismo con Funciones:
#Creamos dos funciones, sumar() y concatenar(), que aceptan diferentes tipos de argumentos:

def sumar(a, b):
    return a + b

def concatenar(a, b):
    return str(a) + str(b)

#Llamamos a estas funciones con diferentes tipos de datos:

resultado1 = sumar(10, 20)              # Resultado: 30
resultado2 = sumar("Hola, ", "mundo")   # Resultado: "Hola, mundo"


resultado3 = concatenar(123, 456)       # Resultado: "123456"
resultado4 = concatenar("Python", 3.7)  # Resultado: "Python3.7"

print(f"resultado: {resultado1}")
print(f"resultado: {resultado2}")
print(f"resultado: {resultado3}")
print(f"resultado: {resultado4}")
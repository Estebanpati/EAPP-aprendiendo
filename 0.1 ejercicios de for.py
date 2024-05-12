#1. Generar una tabla de multiplicar:

for numero in range(1, 13):
  print(f"Tabla del {numero}:")
  for multiplicador in range(1, 13):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

"""Este ejemplo encuentra y muestra todos los números primos entre 1 y 100:"""
def es_primo(numero):
  if numero <= 1:
    return False
  for divisor in range(2, numero):
    if numero % divisor == 0:
      return False
  return True
primos = []
for numero in range(1, 101):
  if es_primo(numero):
    primos.append(numero)
print(f"Números primos entre 1 y 100: {primos}")


"""Este ejemplo genera y muestra los 15 primeros números de la serie de Fibonacci:"""
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(15):
  print(fibonacci(i))


"""Este ejemplo invierte el orden de los caracteres de una cadena de texto:"""
cadena = "Hola, mundo!"
cadena_invertida = ""
for letra in cadena:
  cadena_invertida = letra + cadena_invertida
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {cadena_invertida}")


"""Este ejemplo ordena una lista de números de menor a mayor utilizando el método de la burbuja"""
def burbuja(lista):
  n = len(lista)
  for i in range(n):
    for j in range(n - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
lista = [5, 2, 4, 1, 3]
burbuja(lista)
print(f"Lista ordenada: {lista}")


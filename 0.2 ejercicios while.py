
print(f"A PARTIR DE AQUI ES WHILE")
contador = 1
while contador < 10:
    print(contador)
    contador = contador + 1 #es igual contador += 1

print(f"A PARTIR DE AQUI ES WHILE")

"""Imprimir números pares del 1 al 10"""
numero = 1
while numero <= 10:
  if numero % 2 == 0:
    print(numero)
  numero += 1

"""Contar la cantidad de vocales en una cadena"""
cadena = "Hola, mundo!"
vocales = 0
for letra in cadena:
  if letra in "aeiouAEIOU":
    vocales += 1
print(f"La cadena '{cadena}' tiene {vocales} vocales.")

"""Sumar los números de una lista"""
lista = [5, 3, 7, 1, 4]
suma = 0
for numero in lista:
  suma += numero
print(f"La suma de los números en la lista es: {suma}")


"""Calcular la potencia de un número"""
base = 2
exponente = 4
potencia = 1
while exponente > 0:
  potencia *= base
  exponente -= 1
print(f"{base} elevado a la potencia {exponente} es: {potencia}")

""" Imprimir un patrón de asteriscos"""
filas = 5
while filas > 0:
  print("*" * filas)
  filas -= 1

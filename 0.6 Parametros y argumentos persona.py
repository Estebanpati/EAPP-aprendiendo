
"""def persona(nombre, apellido):
    #Regrese un diccionario con la informacion de una persona
    persona = {'nombre': nombre, 'apellido': apellido}
    return persona
musicoo = persona('Esteba', 'pati')
print(musicoo)"""

def persona(nombre, apellido, edad=''):
    #Regrese un diccionario con la informacion de una persona
    persona = {'nombre': nombre, 'apellido': apellido}
    if edad:
        persona['edad'] = edad
    return persona
musicoo = persona('Esteba', 'pati', edad=33)
print(musicoo)
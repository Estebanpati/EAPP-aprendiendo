
"""def descripcion_mascota(tipo, nombre):
    print("Mi mascota es un " + tipo + ".")
    print("Mi  " + tipo + " se llama " + nombre.title() + ".")
descripcion_mascota('haster','harry')
descripcion_mascota('perro','Fido')"""

#kivo argumentos o argumentos por palabra clave, asocian el nombre y valor

"""def descripcion_mascota(tipo, nombre):
    print("Mi mascota es un " + tipo + ".")
    print("Mi  " + tipo + " se llama " + nombre.title() + ".")
descripcion_mascota(tipo='haster',nombre='harry')
descripcion_mascota(nombre='harry', tipo='haster')"""


def descripcion_mascota(nombre, tipo='perro'):
    print("Mi mascota es un " + tipo + ".")
    print("Mi  " + tipo + " se llama " + nombre.title() + ".")
descripcion_mascota('Fido')


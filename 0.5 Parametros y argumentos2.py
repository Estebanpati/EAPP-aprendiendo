
"""def nombre_con_formato(primer_nombre, segundo_nombre, apellido):
    nombre_completo = primer_nombre + " " + segundo_nombre + " " + apellido
    return nombre_completo.title()
musico = nombre_con_formato('jimi', 'Carlos', 'mamani')
print(musico)"""

#no todos tiene segundo apellido, entonces hacemos lo siguiente
def nombre_con_formato(primer_nombre, apellido, segundo_nombre=''):
    if segundo_nombre:
        nombre_completo = primer_nombre + " " + segundo_nombre + " " + apellido
    else:
        nombre_completo = primer_nombre + " " + apellido
    return nombre_completo.title()
musico = nombre_con_formato('jimi','mamani')
print(musico)

musico = nombre_con_formato('Luis', 'Carlos', 'Llanco')
print(musico)
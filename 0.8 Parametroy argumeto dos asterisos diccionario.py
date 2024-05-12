
def construir_perfil(nombre, apellido, **info_usuario):
    #Construye un diccionario con la informacion del usuario
    perfil = {}
    perfil['primer_nombre'] = nombre
    perfil['apellido'] = apellido
    for clave, valor in info_usuario.items():
        perfil[clave] = valor
    return perfil
perfil_usuario = construir_perfil('albert', 'einstein', ubicacion='princeton', campo='fisica')
print(perfil_usuario)
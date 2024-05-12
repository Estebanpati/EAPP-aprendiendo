
"""def crear_pizza(*toppings):
    #El asterisco puesto al principio le dice a python que construya una tupla llamado toppings y almacene cualquier valor que reciba en esa tupla
    print("Se esta preparando tu pizza con los sigueintes toppibgs:")
    for topping in toppings:
        print("- " + topping)
crear_pizza('peperoni')
crear_pizza('champiñones', 'aceitunas', 'queso extra')"""


def crear_pizza(tamaño, *toppings):
    #El asterisco puesto al principio le dice a python que construya una tupla llamado toppings y almacene cualquier valor que reciba en esa tupla
    print("Se esta preparando tu pizza " + str(tamaño) + " con los sigueintes toppibgs:")
    for topping in toppings:
        print("- " + topping)
crear_pizza('mediano', 'peperoni')
crear_pizza('grande', 'champiñones', 'aceitunas', 'queso extra')


class Pato:
    def hablar(self):
        print('Cua cua')

class Perro:
    def hablar(self):
        print('Guau Guau')

class Gato:
    def hablar(self):
        print('Miau Miau')

def llama_hablar(objeto):
    objeto.hablar()

#Creamos instancias de las clases
pato = Pato()
perro = Perro()
gato = Gato()

#Llamamos a la funcion con diferentes objetos

llama_hablar(pato)
llama_hablar(perro)
llama_hablar(gato)
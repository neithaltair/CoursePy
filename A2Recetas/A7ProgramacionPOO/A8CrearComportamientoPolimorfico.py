#Receta Python 7-8: Crear comportamiento polimorfico

class Perro():
    def hacerSonido(self):
        print("guau")

class Gato():
    def hacerSonido(self):
        print("miau")

def hacerSonido(animal):
    animal.hacerSonido()


gato = Gato()
perro = Perro()
loro = Gato()

hacerSonido(gato)
hacerSonido(perro)
hacerSonido(loro)
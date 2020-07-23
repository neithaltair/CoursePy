# A7-5: Crear un objeto

#Para las clases, la primera en mayuscula

class Persona:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    #Metodo que sobreescribe el metodo de representacion de caracteres
    def __str__(self):
        return "Nombres: {} - Edad {} - ID: {}".format(self.nombre, self.edad, self.id)

fernanda = Persona('Fer Gomez', 30, '123456789')

print(fernanda)
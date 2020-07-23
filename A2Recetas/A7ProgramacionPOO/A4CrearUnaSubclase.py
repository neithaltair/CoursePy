#Receta 7-2: crear una clase

#Para las clases, la primera en mayuscula

class Persona:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    #Metodo que sobreescribe el metodo de representacion de caracteres
    def __str__(self):
        return "Nombres: {} - Edad {} - ID: {}".format(self.nombre, self.edad, self.id)


class Empleado(Persona):
    def __init__(self, nombre, edad, id, salario):
        super(Empleado, self).__init__(nombre, edad, id)

        self.salario = salario

         
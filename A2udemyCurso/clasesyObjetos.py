class claseSilla:
    color = "blanco"
    precio = 100

objetoSilla = claseSilla()

print(objetoSilla.color)
print(objetoSilla.precio, "\n")

objetoSilla1 = claseSilla()

objetoSilla1.color = "verde"
objetoSilla1.precio = 300

print(objetoSilla1.color)
print(objetoSilla1.precio)


print("\nCLASE PERSONA ")
class Persona :
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre

    def saludar(self):
        print("Mi nombre es {} y tengo esta edad {}".format(self.nombre, self.edad))

persona1 = Persona("Fredy",54)

print(persona1.edad, persona1.nombre)

persona1.saludar()
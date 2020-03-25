#CREAR UNA CLASE "COCHE" QUE TENGA ESTOS ATRIBUTOS:
#MARCA, COLOR, COMBUSTIBLE, Y CILINDRADA
#CREAR LA FUNCION INIT QUE ASIGNA LOS PARAMETROS DE LA CLASE A LOS ATRIBUTOS DE LA CLASE
#CREAR OTRA FUNCION "MOSTRAR CARACTERISTICAS" QUE MEDIANTE PRINT MUESTRE POR PANTALLA
#LAS CARACTERISTICAS (O ATRIBUTOS) QUE TIENE EL COCHE
#CREAR UN OBJETO "COCHE1" DE LA CLASE "COCHE" CON LOS ATRIBUTOS "OPE1", "ROJO", "GASOLINA","1.6"
#EJECUTAR LA FUNCION "MOSTRAR CARACTERISTICAS" DEL OBJETO "COCHE1"

class coche:
    def __init__(self, marca, color, gasolina, cilindrada):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina
        self.cilindrada = cilindrada

    #marca = input("ingrese = ")


    def mostrarCaracteristicas(self):
        print("Marca = {}, Color = {}, Gasolina = {}, Cilindrada = {}".format(self.marca, self.color, self.gasolina, self.cilindrada))


coche1 = coche(input("Marca = "), input("Color = "), input("Gasolina = "), input("Cilindrada = "))

print(coche1.mostrarCaracteristicas())

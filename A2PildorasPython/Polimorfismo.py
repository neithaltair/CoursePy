class Coche():

    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")

miVehiculo = Coche()
miVehiculo.desplazamiento()


def desplazamientoVehiculo(vehiculo):
    #Usara el objeto por parametro para llamar el metodo desplazamiento
    vehiculo.desplazamiento()


miVehiculo1 = Camion()
desplazamientoVehiculo(miVehiculo1)


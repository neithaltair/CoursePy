class Coche():

    #Creacion del  constructor
    def __init__ (self):
        self.largoChasis=250
        self.anchoChasis=120
        #En este punto se hace un encapsulamiento de la variable ruedas
        self.__ruedas=4
        self.enmarcha=False
        self.gasolina = 0


    #Establecemos un metodo donde creamos la variabe arrancamos para posteriormente asignarle un valor el cual
    #sera el nuevo valor de la variable en marcha en el constructor
    def arrancar(self, arrancamos):

        self.enmarcha = arrancamos

        #if (self.enmarcha):
        chequeo = self.__chequeoInterno()

        if(self.enmarcha == True and chequeo == True):
            return "El coche esta en marcha"

        elif(self.enmarcha and chequeo ==False):
            return "ALgo ha salido mal"


        else:
            return "El coche no esta prendido"

        #self.enmarcha=True


    #Se crea este metodo para que imprima el estado del coche
    def estado(self):

        # Si el carro tiene gasolina, el chequeo fue correcto y lo prendieron informa que el carro esta prendido
        if(self.enmarcha == True and self.gasolina > "0" and self.__chequeoInterno() == True):

            print("El carro esta prendido, tiene ", self.__ruedas, "ruedas, un largo de ",
            self.largoChasis, "metros, Un ancho de ", self.anchoChasis, " metros")

        #si el carro no tiene gasolina el carro no prende
        else:
            print ("El carro esta apagado")


    #Establesco  el metodo de tanquear donde paso la gasolina de 0 a 100
    def tanquear(self):
        self.gasolina = "100"




    #Metodo para verificar esstado del carro metodo encapsulado
    def __chequeoInterno (self):
        print("Realizando el chequeo del carro")

        #self.gasolina="ok"
        self.aceite="ok"
        self.puertas = "cerradas"

        if (self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



#Instancio la clase 1
miCoche = Coche()



#Llamo los metodos de arrancar y tanquear el carro para que se pueda prender
miCoche.tanquear()

#a la variable arrancamos le pasamos el valor de TRUE
print(miCoche.arrancar(True))


#Imprimo el estado del carro
miCoche.estado()


print("\n\n-----------------A continuacion creamos el segundo objeto--------------\n\n")

#Segunda instancia de la clase
miCoche1 = Coche()


miCoche1.tanquear()
print(miCoche1.arrancar(True))

#Este cambio en la cantidad de ruedas no se ejecuta debido a que la variable esta encapsulada
miCoche1.ruedas = 6

miCoche1.estado()

class Vehiculos():

    # SE DEFINE EL CONSTRUCTOR
    def __init__ (self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo

        self.acelera = False
        self.frena = False
        self.enciende = False


    #SE ESTABLECEN LOS METODOS QUE TENDRAN LOS VEHICULOS
    def arrancar (self):
        self.acelera = True

    def frenar (self):
        self.frena = True

    def encender(self):
        self.enciende = True


    #INDICARA EL ESTADO Y QUE TIPO DE VEHICULO ES 
    def estado (self):
        print("Marca = ", self.marca, "\nModelo = ", self.modelo, "\nEnciende = ",self.enciende, "\nAcelerando = ",
        self.acelera, "\nFrenando = ", self.frena)



#=========================COMIENZO DE LA CLASE FURGONETA===============================================
#NUEVA CLASE DE CARRO
#furgoneta va a heredar de vehiculos donde heredara marca y modelo
class Furgoneta(Vehiculos):

    #Creamos un metodo carga que nos indicara si la furgoneta esta cargada
    def carga(self, cargar):


        self.cargado = cargar

        if(self.cargado == True):
            return "Furgoneta cargada"
        else:
            return "Furgoneta no cargada"






#==================COMIENZO DE EL VEHICULO MOTO==========================================================
# UBICANDO EL VEHICULOS EN LOS PARENTESIS YA PYTHON SABE QUE ES HERENCIA
class Moto(Vehiculos):
    #Creamos la variable hcaballito vacia
    hcaballito = ""

    #definimos el metodo caballito el cual le data un valor a la variable 
    # de "Voy haciendo manual"
    def caballito (self):
        #al llamara a este metodo la moto hara caballito
        self.hcaballito = "Voy haciendo manual"

    #heredamos el metodo de estado y anexamos el contenido de la variable
    #hcaballito para que lo imprima
    def estado(self):
        super().estado()

        print(self.hcaballito)


#______________________________________________________________________________



#======================CLASE DE VEHICULOS ELECTRICOS
class vElectricos(Vehiculos):
    #Establecemos el constructor de vElectricos donde hereda de vehiculos
    def __init__(self, marcaBici, modeloBici, autonomia):

        #Hace el llamado al constructor de la clase padre e indica que variables
        #seran las que usaremos de esta clase
        super().__init__(marcaBici, modeloBici)
        
        #la variable autonomia la asignaremos nosotros
        self.autonomia = autonomia 
    

    def cargarEnergia(self):
        self.cargando = True

    #funcion heredada para saber el estado del vehiculo y agregar
    # una nueva impresion
    def estado(self):

        super().estado()
        print("Autonomia = ",self.autonomia)

#_____________________________________________________________________


#HERENCIA MULTIPLE, SE LE DA PRIORIDAD A LA CLASE QUE SE UBICA DE PRIMERAS
#ESTABLECEMOS QUE HAREMOS HERENCIA DE DOS CLASES VEHICULOS Y VEHICULOS ELECTRICOS
class biciElectrica(vElectricos, Vehiculos):

    #En el constructor indicamos las variables a usar
    def __init__(self, marca, modelo, autonomia):
        
        #Las tres variables seran heredadas
        super().__init__(marca, modelo, autonomia)

    #Para saber el estado del vehiculo tambien haremos herencia
    def estado(self):
        super().estado()



# instanciamos miBici con vehiculos electricos y agregamos marca, modelo
# y autonomia 





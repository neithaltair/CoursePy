#Crear el modulo "moduloficheros.py"
#Crear una clase "Fichero"
#Crear la funcion "leer_fichero" para leer de un fichero de texto
#Crear la funcion "grabar_fichero" para crear un fichero de texto
#Crear la funcion "incluir_fichero" para incluir datos al final de un fichero de texto

class fichero:
    #La variable nombre hace referencia a el nombre que tendra el fichero
    def __init__(self, nombre):
        self.nombre = nombre

    # El texto se pasara como parametro de la funcion
    def crearFichero(self, texto):

        fichero2 = open(self.nombre, "wt")
        fichero2.write(texto)
        fichero2.close()


    def anexarFichero(self, texto):

        fichero1 = open(self.nombre,"at")
        fichero1.write(texto)
        fichero1.close()


    def leerFichero(self):

        fichero = open(self.nombre,"rt")
        leerdatos = fichero.read()
        return leerdatos
        fichero.close()
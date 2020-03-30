#Crear un programa "programa1.py"
#crear el objeto "fichero" de la clase "Fichero" del modulo "moduloficheros.py"
#utilizar el metodo "grabar fichero" del objeto fichero del modulo modulo ficheros
#utilizar el metodo "incluirfichero" para incorporar mas datos al final del fichero
# utilizar el metodo "leer_fichero" para ver todos el contenido del fichero

import moduloFicheros


nombre_fichero = input("Nombre del archivo")+'.txt'
fichero = moduloFicheros.fichero(nombre_fichero)

texto = input("Con que contenido desea iniciar el archivo")
fichero.crearFichero(texto)

texto = input("Desea agregar un nuevo contenido al archivo")
fichero.anexarFichero(texto)


textoLeido = fichero.leerFichero()
print(textoLeido)

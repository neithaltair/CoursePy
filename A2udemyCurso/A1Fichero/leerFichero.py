#se abrira un archivo de texto en modo lectura "r"
#que contiene texto (caracteres) "t"
#Metodo open devuelve los datos del texto y se almacenan en la variable fichero
fichero = open("leerTexto.txt", "rt")

#para leer el contenido del texto se debe llamar el metodo read
#se asigna el contenido del texto a la variable datos_fichero
datos_fichero = fichero.read()

print(datos_fichero)

fichero.close()
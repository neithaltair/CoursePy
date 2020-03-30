#Agregar nueva informacion al fichero
#A= hacer referencia al append, que es agregar informacion
#T= Hace referencia a que sera contendio texto(caracteres)

fichero = open("anexarTexto.txt","at")

#Haciendo uso de el salto de linea y concatenando el input
#Se logra que el contenido nuevo haga parte de un nuevo renglon
#en el texto
cadenaIncluir ="\n" + input("Ingrese la nueva linea = ")

fichero.write(cadenaIncluir)

fichero.close()

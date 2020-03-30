#Crear un fichero de texto
#W = significa que sera de escritura
#T = significa que sera de texto, (Caracteres)
#fichero = open("crearTexto.txt", "wt")


#contenidoFichero = "Este es el contenido que ira en el fichero"
#fichero.write(contenidoFichero)


#fichero1 = open("crearTexto.txt", "rt")

#leerfichero = fichero1.read()

#print(leerfichero)

#fichero.close()

#Cracion de dos variables, una en false y otra en 0
estado = False
cont = 0

#se establece la creacion de creart texto
fichero = open("crearTexto.txt", "wt")

#se establece el contenido para agregar y crear el texto
contenidoFichero = "Este es el contenido que ira en el fichero"
fichero.write(contenidoFichero)

#Se cambia el contenido de las variables
estado = True
cont+=1

#cerrado del fichero
fichero.close()


#se establece un condicional para ver las impresion del texto luego de crearlo
if (estado == True) and (cont != 0):
    #respectivo open del texto
    fichero1 = open("crearTexto.txt", "rt")
    #se crea la variable encagada de leer el contenido
    leerfichero = fichero1.read()
    #se imprime el contenido en pantalla
    print(leerfichero)

    fichero1.close()






#Leer contenido de un archivo

# 1. leer todo el contenido
# 2. leer una parte
# 3. utilizar un ciclo

archivo = open('paises.csv')

#LEE TODO EL CONTENIDO DEL ARCHIVO
#print(archivo.read())

#LECTURA PARCIAL, lee una parte segun los bytes que se psen
#lecturaParcial = archivo.read(10)
#print(lecturaParcial)

#3 uso de un ciclo para recorrer el archivo:
for linea in archivo:
	#Para evitar el salto de linea al imprimir, se usa el end con caracter vacio
	print(linea, end='')
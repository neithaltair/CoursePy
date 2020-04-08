# Expresiones regulares (search, findall, aplit, sub)

texto = "Hola, mi nombre es Neith Altair"
#Se hace la importacion del modulo
import re

#Se hace uso del re y search para buscar el contenido nombre en el texto
print(re.search("nombre",texto))

#Se puede hacer la asignacion del re.search a una variable
restultado = re.search("^Hola", texto)

if (restultado):
    print("Se encontro el nombre")
else:
    print("no hay compatibilidad")



#Se puede hacer uso del signo peso para que busque la palabra
#En la ultima posicion Altair$

#Para realizar la busqueda iniciando con una palabra
# ^Hola

#Relacionar dos palabras en un texto
# (mi .* es)    el punto y el asterisco sirven para remplazar los valores en medio

#
#Receta 5-8 : Explorar los registros de un DataFrame
#head devuelve los primeros 5 registros, Tail devuleve los ultimos registros
#head() y tail()

import pandas as pd

peliculas = pd.read_csv("movies.csv")

#Si al head le damos un valor, imprimira la cantidad de registros asignados e.g: head(30)
print("\nImpresion de las los primeros 5 registros = \n",peliculas.head(20))

#Ver la cantidad de columnas que tiene el documento
#print("\nImprime las columnas que tiene el documento = \n",peliculas.columns)

#El tail imprime los ultimos 5 registros, tambien se puede asignar un valor e.g: tail(18)
print("\nImprime los ultimos registros del documento\n",peliculas.tail(10))

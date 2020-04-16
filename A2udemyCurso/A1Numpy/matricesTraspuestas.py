#Cambiar ordenadamente las filas por las columnas
import numpy as np

#Tres filas por 5 columnas
array = np.arange(15).reshape((3,5))
print(array)

#Posicion del elemento en el array
print(array[1][1])

#Cambiar las filas por columnas
arrayTras = array.T
print(arrayTras)
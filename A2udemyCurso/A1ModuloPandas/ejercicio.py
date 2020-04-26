#Tenemos 3 clases  "clase1" hasta la clase 3
#Vamos a fenerar un numero alatorio de alumnos por clase
#para obtener un numero aleatorio utilizaremos
#np.random.randit(minimo, maximo, numero)

#Crear una clase de alumnos, utilizar el indic de la alerta para saber
#el numero de alumnos en la clase2

import pandas as pd
import numpy as np

min = 10
max = 40
num = 3
#Numero de alumnos aleatorio de cada clase
#implementacion del  randint para que sean enteros
alumnos = np.random.randint(min,max, num)

print("\nCantidad de alumnos por clase =\n",alumnos)

clases = ['clase1','clase2','clase3']

series = pd.Series(alumnos, index=clases)

print("\nImprime la serie de clases y alumnos =\n",series)

#Saber la cantidad de alumnos en la clase 2
print("\nClase y cantidad alumnos especifico=\n",series['clase3'])



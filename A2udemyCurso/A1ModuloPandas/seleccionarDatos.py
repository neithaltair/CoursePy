#Seleccionando datos de una serie

import pandas as pd
import numpy as np

listaValores = np.arange(9)
print(listaValores)

listaIndi = ['a','b','c','d','e','f','g','h','i']
serie = pd.Series(listaValores, index=listaIndi)

print(serie)


#Para hacer la multiplicacion de cada uno de los valores
# por un numero especifico se implementa de la siguiente manera

serie = serie * 60
print('\nSerie multiplicada por 2 = \n',serie)


#Acceder a los elementos se puede acceder a ellos por el indice
print('\nAccediendo a un elemento por el indice [d]=\n',serie['d'])

#Tambien se puede acceder posicionalmente
print('Accediendo a un elemento por posicion [6]=\n',serie[6])

#Acceder a multiples elementos
print('Acceder a multiples elementos [0:6] =\n',serie[2:6])

#Se pueden seleccionar los elementos que cumplan una condicion
print('\nElementos que cumplen con la condicion (serie>200)\n',serie[serie>200])

#Se le puede cambiar el valor de un elemento
serie[serie>200] = 9999
print("\nSe cambian los valores de la serie cuando son mayores a [serie>200] = 9999\n",serie)



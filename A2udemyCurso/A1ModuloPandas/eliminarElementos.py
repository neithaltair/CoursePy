#Eliminar elementos y dataFrames

import pandas as pd
import numpy as np


#Numpy se usa para un arreglo
print(np.arange(3))

serie = pd.Series(np.arange(4), index=['a','b','c','d'])

print(serie)

#Eliminar un elemento
serie.drop('c')

#Crear un dataFrame con indices y columnas
print("\nDataFrame con indices y columnas, 3 filas 3 columnas, el\n"
      "range imprime del 0 al 8 y el reshape indica cuantas filas\ny cuantas"
      "columnas se van a utilizar=\n",np.arange(9).reshape(3,3))




#Se creara el dataframe a partir de la lista de valores se pasa
# el indice y las columnas
listaValores = np.arange(60).reshape(5,12)

listIndice = ['a','b','c','d','e']
listColumn = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12']

dataFrame = pd.DataFrame(listaValores, index=(listIndice), columns=(listColumn))

print('\nRealiza la impresion del data Frame\n'
      'luego de asignarles los valores establecidos\n',dataFrame)

#para eliminar una fila del data frame se hace uso del drop
print('\nImpresion del dataFrame luego de eliminar fila (d)\n',dataFrame.drop('d'))

#Para eliminar la columna se hace uso del drop pero se añade el axis
print('\nSe hace eliminacion de la columna c7 haciendo uso del drop y de\n'
      'el axis\n',dataFrame.drop('c7', axis=1))



#Para mantener los cambios realizados al dataFrame se deben asignar a la variable de
#data frame Ejemplo = 

dataFrame = dataFrame.drop('c7',axis=1)
import pandas as pd
import numpy as np

#Genera numeros del 0 al 8 y lo pone en una forma de 3x3 3filas x 3columnas
array1 = np.arange(9).reshape(3,3)
print("Imprime el array creado",array1)

#Realiza la concatenacion hacia abajo
print("\nImprime la concatenacion hacia abajo\n",np.concatenate([array1,array1]))

#para realizar la concatenacio hacia la derecha, mediante axis
print("\nImprime el array al lado haciendo uso de axis\n",np.concatenate([array1,array1], axis=1))

#Concatenacion de series
serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([4,5,6], index=['d','e','f'])

#Para concatenar la series
print("\nCONCATENACION DE SERIES")
serieConcat = pd.concat([serie1,serie2])
print("Imprime la concatenacion de las series\n",serieConcat)

print("\nImprime la serie 1\n",serie1)
print("\nImprime la serie 2\n",serie2)

#Para identificar las series dentro de la concatenacion se puede hacer uso de keys
keys = pd.concat([serie1,serie2], keys=['Serie1','Serie2'])
print("\nImprime la concatenacion, identificando las series en ella\n",keys)


#Concatenacion de dataFrames
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a','b','c'])
print("\nImprime el dataFrame por separado\n",dataframe1)

dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a','b','c'])
print(dataframe2)

#Concatenacion de los dataFrames creados
# con el uso de ignore index logramos ignorar los index de cada dataFrame y crea uno nuevo
dataConcat = pd.concat([dataframe1, dataframe2], ignore_index=True)
print("\nLos dos DataFrames concatenados\n",dataConcat)

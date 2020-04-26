#Estadisticas en dataframe
import pandas as pd
import numpy as np
#Crea un array
array = np.array([[1,5,6],[8,5,9]])
#Imprime el array
print(array)
#Crea un data frame con la informacion del array, se agregan filas y columnas
dataframe = pd.DataFrame(array, index=['a','b'], columns=['a1','b1','c1'])
print(dataframe)

#Ejecucion de suma por columnas
print("\nEjecucion de suma por filas =\n",dataframe.sum())


#Minimo valor por columnas
print('\nMinimo valor por columnas =\n',dataframe.min())

#Saber valor maximo
print('\nSaber valor maximo =\n',dataframe.max(axis=1))

#Saber por index el numero mayor
print('\nSaber por index el numero mayor =\n',dataframe.idxmax())

#Data Frame .describe
print("\nArroja estadisticas sobre los numeros en la serie =\n",dataframe.describe())
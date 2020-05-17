import pandas as pd
import numpy as np

listaValores = [[1,2,3], [4,5,6], [7,8,9], [np.nan, np.nan, np.nan]]

print(listaValores)

listaColumnas = list('abc')
print(listaColumnas)

#CREACION DEL DATAFRAME
dataFrame = pd.DataFrame(listaValores, columns=listaColumnas)
print("\nimprime data Frame con valores nulos\n",dataFrame)

#REALIZA LA SUMA E IMPRIME EL NUMERO MENOR POR COLUMNA
#suma significa la suma, min significa el numero menor
valor = dataFrame.agg(['sum','min'])
print("\nSuma la columna e imprime el minimo\n",valor)

#REALIZA LA SUMA POR FILAS
filas = dataFrame.agg("sum", axis=1)
print("\nImprime la suma por filas\n",filas)
import pandas as pd
import numpy as np

#Creacion de la lista con valores
listaValores = [[1,2,3],[4,np.nan,6],[7,8,np.nan]]
print('Imprime lista de valores =',listaValores)

listaIndice = list('ABC')
listaColumn = list('DEF')

#Creacion del dataframe agregando indices columbas y valores
dataFrame = pd.DataFrame(listaValores, index=listaIndice, columns=listaColumn)

print(dataFrame)

#Saber si hay valores nulos en le data
print("\nSaber si hay valores nulos en le dataFrame\n",dataFrame.isnull())

#Rellenar valores nulos de manera rapida
dataFrame = dataFrame.fillna(5)

print("\nImprime data Frame=\n",dataFrame)
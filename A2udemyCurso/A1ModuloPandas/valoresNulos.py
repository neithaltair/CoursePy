#VALORES NULOS

import pandas as pd
import numpy as np

#Lista de valores con elemento nulo
listaValores = ['1','2',np.nan,'4']

print(listaValores)

#Serie
serie = pd.Series(listaValores, index=list('AGTW'))
#Imprime la serie
print("\nRealiza la impresion de la serie =\n",serie)

#Se puede verificar si un elemento es nulo con .isnull
print("\nVerificacion con isnull si hay vlr nulo =\n",serie.isnull())

#Se pueden borrar los valores nulos con dropna
print("\nImprime la serie dejando el valor nulo por fuera=\n",serie.dropna())

#Borra el valor nulo de manera permanente
serie = serie.dropna()



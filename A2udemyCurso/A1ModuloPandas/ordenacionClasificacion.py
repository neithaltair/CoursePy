#Ordenar y clasificar series
import pandas as pd
import numpy as np

#print(range(5))

#se crean los valores con range hasta 10
listaValores = range(10)
#se crean los indices con 10 letras
listaIndic = list('ASDFGHJKLP')

#Creacion de la serie con pandas
serie = pd.Series(listaValores, index=listaIndic)

print(serie)

#Organizar la serie por el index
print("\nOrden del index alfabeticamente =\n",serie.sort_index())

#Ordenar la serie por los valores
print("\nOrdena serie por los valores = \n",serie.sort_values())

#Hacer un Ranking
print("\nImprime un ranking = \n",serie.rank())
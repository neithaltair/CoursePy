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


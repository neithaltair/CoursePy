# Receta 5-3: Crear un objeto panel

import pandas as pd 

paises = pd.read_csv('paises.csv')

#Imprime las columnas del dataFrame
print("\nImprime las columnas del dataFrame\n",paises.columns)

#Tamaño/Forma del DataFrame
print("\nForma, Tamaño del DataFrame\n",paises.shape)

#Longitus de registros 
print("\nLongitud de registros\n",len(paises))

#Ver solamente una de las columnas
print("\nVer solamente una de las columnas\n",paises['paises'])
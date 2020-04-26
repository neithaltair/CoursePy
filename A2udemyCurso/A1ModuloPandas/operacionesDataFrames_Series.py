#Operaciones sobre series y dataFrames
import pandas as pd
import numpy as np

listaValores = np.arange(25,50).reshape(5,5)

listaIndice = ['a','b','c','d','e']
listaColumn = ['a1','b1','c1','d1','e1']
#Creacion del data frame
serie = pd.DataFrame(listaValores, index=(listaIndice), columns=(listaColumn) )

print(serie)

listaValores1 = np.arange(50,75).reshape(5,5)
serie2 = pd.DataFrame(listaValores1, index=listaIndice, columns=listaColumn )
print("\nSerie 2 =\n",serie2)

#Se realiza la multiplicacion entre las series
print("\nSumatoria de las series =\n",serie*serie2)

#para completar una columna del dataframe que no contiene valores
#se hace implementacion del
serie2.add(serie, fill_value=10)


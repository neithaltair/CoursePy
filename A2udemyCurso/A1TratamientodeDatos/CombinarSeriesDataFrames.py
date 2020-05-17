#Combinar series y dataFrames
import pandas as pd
import numpy as np

serie1 = pd.Series([1,2,np.nan])
print(serie1)

#Series 2
serie2 = pd.Series([4,5,6])
print(serie2)

#Serie3 SE COMBINAN LAS SERIES CON COMBINE_FIRST
#Remplaza el valos nullo por el valor de la serie 2 en la misma posicion
serie3 = serie1.combine_first(serie2)
print("\nImprime la combinacion de las dos series\n",serie3)


#DATAFRAMES
listaValores = ([1,2,np.nan])
dataFrame1 = pd.DataFrame(listaValores)

print("\nImpresion del dataframe\n",dataFrame1)

#Segundo DATAFRAME
listaValores1 = ([4,5,6])
dataFrame2 = pd.DataFrame(listaValores1)

print("\nImprime el segundo DataFrame\n",dataFrame2)

#Combinacion de los dataFrames
dataFrame3 = dataFrame1.combine_first(dataFrame2)

print("\nRealiza la impresion de los dos dataFrames combinados\n",dataFrame3)
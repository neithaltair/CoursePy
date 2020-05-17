#Agrupacion DataFrames

import pandas as pd
import numpy as np

listaValores = {'clave1':['x','x','y','y','z'], 'clave2':['a','b','a','b','a'], 'datos1':np.random.rand(5),'datos2':np.random.rand(5)}

print(listaValores)

#Imprime el data frame con la informacion de listaValores
dataFrame = pd.DataFrame(listaValores)
print("\nImprime el dataFrame con los valores asignados\n",dataFrame)

grupo1 = dataFrame['datos1'].groupby(dataFrame['clave1'])
print(grupo1)


#Se imprime la agrupacion de datos1 con la clave uno
# y por medio de mean se obtiene el promedio
print("\nImprime el promedio\n",grupo1.mean())
#Recetas 5-11 Aplicar una funcion sobre una fila o columna
import numpy as np
import pandas as pd

datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
#SE establece el data frame
df = pd.DataFrame(data=datos, index=['n','e','i'])

#Se imprime el contenido del DataFrame
print(df.head())

#Obtiene el promedio de cada una de las columnas haciendo uso del numpy(verticalmente)
print("\nImprime promedio columna\n",df.apply(np.mean))

#Aplicar Funciones por fila, obtiene el promedio de la fila (horizontalmente)
print("\nImprime fila de la columna =\n",df.apply(np.mean, axis=1))

#Haciendo uso de lambda, multiplica los valores por dos
print("\n",df.apply(lambda x: x * 2, axis=0))
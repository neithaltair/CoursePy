#FILTRAR UN DATAFRAME
#CREAREMOS UNA LISTA DE 50 VALORES ALEATORIOS ENTEROS ENTRE LOS VALORES 0 Y 100
#CONVERTIREMOS ESTA LISTA EN UN DATAFRAME CON 5 FILAS Y 10 COLUMNAS
#FILTRAREMOS LOS DATOS DEL DATAFRAME PARA VISUALIZAR SOLO LOS VALORES QUE SEAN MAYORES DE 50

import pandas as pd
import numpy as np

listaValores = np.random.randint(0,100,50).reshape(5,10)
print(listaValores)

#SI NO SE HACE USO DEL RESHAPE SE PUEDE USAR EL RESIZE
#listaValores.resize(5,10)
#print(listaValores)

dataFrame = pd.DataFrame(listaValores)
print("\nImpresion del DataFrame con los valores\n",dataFrame)

#IMPRIME EL DATAFRAME CON LOS VALORES MAYORES A 50
print("\nNumeros mayores a 50 en el DataFrame\n",[dataFrame[dataFrame>50]])
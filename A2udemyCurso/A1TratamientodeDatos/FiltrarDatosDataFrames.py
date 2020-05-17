import pandas as pd
import numpy as np

#10 filas por 3 columnas
listaValores = np.random.rand(10,3)
#Imprime la lista aleatoria
print(listaValores)

#Agrega los valores random al dataFrame
dataFrame = pd.DataFrame(listaValores)
print("\nImprime los valores del dataframe con los numeros random\n",dataFrame)

#Imprime una columna especifica
columna0 = dataFrame[0]
print("\nImprime una columna especifica\n",columna0)

#imprimir mayores a 0.40
print("\nImprime los valores mayores a 0.40\n",columna0[columna0>0.40])

#seleccionar mayores a en el DataFrame
print("\nImprime mayores a 0.50 en todo el DataFrame\n",[dataFrame[dataFrame>0.50]])
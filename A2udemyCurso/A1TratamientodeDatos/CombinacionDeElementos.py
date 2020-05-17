import pandas as pd
import numpy as np

listaValores = np.arange(25).reshape(5,5)
print(listaValores)

dataFrame = pd.DataFrame(listaValores)
print("\nImprime el data Frame\n",dataFrame)

#Combinacion aleatoria
combinacionAleatoria = np.random.permutation(5)
print("\nImpresion de Valores Aleatorios\n",combinacionAleatoria)

#Invierte las filas del DataFrame
combi = dataFrame.take(combinacionAleatoria)
print("\nImprime la combinacion\n",combi)


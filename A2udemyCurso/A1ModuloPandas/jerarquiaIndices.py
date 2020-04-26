#Jerarquia de los indices
import pandas as pd
import numpy as np
#Se crea la serie con 8 numeros aleatorios
listaValores = np.random.rand(8)
#Print inprime los numeros aleatorios
#print(listaValores)

#Creacion de lista de indices
listaIndic = [[1,1,1,1,2,2,2,2],['a','b','c','a','b','c','a','b']]

series = pd.Series(listaValores, index=listaIndic)
print('\nImprime la serie con indice de primer y segundo nivel =\n',series)

#Acceder a un valor en concreto
print('\nAcceder a valor en concreto = \n',series[1]['b'])

#Convertir una serie con dos indices a una serie con indice y columnas
#haciendo uso de "unstack"

#dataFrame = series.unstack()
#print(dataFrame)


#Crear un dataframe y convertirlo a una serie
lista1 = np.arange(16).reshape(4,4)
print("\n",lista1)

#Generacion de indices y columnas
listaI = list('1234')
listaC = list('AHSE')

dataframe = pd.DataFrame(lista1, index=listaI, columns=listaC)

#Se imprime el dataFrame con index y subindices
print("\nData frame\n",dataframe)

#A partir del Data Frame, crear una serie con doble indice
serie2 = dataframe.stack()
print("\nA partir del Data Frame, crear una serie con doble indice = \n",serie2)
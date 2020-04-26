import pandas as pd
import numpy as np

listaValores = np.arange(25,50).reshape(5,5)

print(listaValores)


listaIndice = ['a','b','c','d','e']
listaColumn = ['a1','b1','c1','d1','e1']
#Creacion del data frame
serie = pd.DataFrame(listaValores, index=(listaIndice), columns=(listaColumn) )
#Impresion del data frame
print("\nImprime la serie con indices y columnas =\n",serie)


#acceder a un dataFrame especifico
print("\nImprime una columna especifica =\n",serie['c1'])

#tambien se puede acceder al indice y la columna
print("\nImprime columna e indice especificos =\n",serie['c1']['d'])

#se puede hacer la seleccion de varias ade las columnas DOBLE COCHETE

print("\nImprime varias columnas especificas =\n",serie[['c1','d1','e1']])

#Seleccionar los valores de columna especifica mayores a:
print("\nImprime en booleano los elementos de columna c1 y e1 "
      "mayores a 39 =\n",serie[['c1','e1']]>39)

#imprimir indice especifico con numeros
print('\nImprimir indice especifico con sus valores usando (loc) =\n',serie.loc['c'])






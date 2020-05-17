#Eliminar duplicados en DataFrames
import pandas as pd

listaValores =[[1,2],[1,2],[5,6],[5,8]]
print(listaValores)

listaIndices = list('mnop')
print(listaIndices)

listaColumnas = ['Valor1','Valor2']
print(listaColumnas)

dataFrame = pd.DataFrame(listaValores, index=listaIndices, columns=listaColumnas)
print("\nRealiza la impresion del DataFrame\n",dataFrame)

#REALIZA LA ELIMINACION DE LAS FILAS DUPLICADAS EN EL DATAFRAME
duplicados = dataFrame.drop_duplicates()
print("\nElimina los valores duplicados\n",duplicados)

#ELIMINAR LOS REPETIDOS DENTRO DE LA MISMA COLUMNA
columna = duplicados.drop_duplicates(['Valor1'])
print("\nElimina los duplicados en columnas\n",columna)

#PARA MANTENER EL ULTIMO VALOR SE DEJA KEEP
columna1 = duplicados.drop_duplicates(['Valor1'], keep='last')
print("\nMantiene el ultimo valor de las columnas\n",columna1)
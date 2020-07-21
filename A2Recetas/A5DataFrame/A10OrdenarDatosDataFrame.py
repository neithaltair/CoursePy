#Ordenar Datos en un DataFrame por indices o por sus columnas

import pandas as pd
datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

#El dataframe se creara con los datos, el index indicara las columnas
df = pd.DataFrame(data=datos, index=['b','c','a'])

#Imprime el data frame basado en la variable datos
#Imprime los registros del DataFrame
print("\nLos primeros registros del DataFrame\n",df.head())

#Ordenar el DataFrame haciendo uso de sort(), ordena las filas (index())
print(df.sort_index())

#SE le puede dar orden a las columnas, con sort_values(by=[columna], ascending=[Bool])
print("\nQue columna se va a ordenar y de que manera asc o desc =\n",df.sort_values(by='col2', ascending=False))


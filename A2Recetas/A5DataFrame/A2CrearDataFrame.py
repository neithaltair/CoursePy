import pandas as pd 

diccionario = {'colum1':[1,2,3,4,5,6], 'colum2':[7,8,9,10,11,51]}

df = pd.DataFrame(data=diccionario)

#Ahead muestra los primeros
#print(df.head())

#Tail muestra los ultimos
print("\nMuestra los ultimos valores\n",df.tail(2))

#Saber como se llaman las columnas
print("\nNombre de las columnas\n",df.columns)

#Estadisticas basicas del dataFrame
print("\nEstadisticas basicas del dataFrame\n",df.describe())

#Solo imprime el contenido de la columna especifica
print("\nSolo imprime el contenido de la columna especifica\n",type(df['colum2']))
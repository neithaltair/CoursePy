#Receta 5-13: Iterar un dataFrame

import pandas as pd

datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

df = pd.DataFrame(data=datos)

#print(df)

#Iteracion por columnas:
for columna in df:
    #Realiza la impresion de las columnas
    #print(columna)

    #Imprime el contenido de las columnas
    print(df[columna])

#Iterar indice Fila:
for indice, fila in df.iterrows():
    print('indice : {}'.format(indice))
    print(fila)
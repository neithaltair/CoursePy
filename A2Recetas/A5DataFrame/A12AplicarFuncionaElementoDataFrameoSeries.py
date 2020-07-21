#Receta 5-12: Aplicar una funcion a cada elemento de unDataFrame o Series
import pandas as pd

datos = datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

#1. applymap: se usa sobre un DataFrame
#2. map: se usa sobre un series

df = pd.DataFrame(data=datos, index=['a','l','t'])

print(df.applymap(lambda x: x **3),"\n")
print(df.applymap(lambda x: x **2))

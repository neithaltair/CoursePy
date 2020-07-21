#PASAR UN DATAFRAME A UN ARCHIVO EXCEL
import pandas as pd 

ids = [1,2,3,4,5]
paisEur = ['albania','Belgica','chipre','eslovenia', 'Dinamarca']

df = pd.DataFrame(data={'id':ids, 'pais':paisEur})

print(df.head())

#sheet_name es para darle un nombre a la hoja, index para no traer las posiciones
df.to_excel('paisEuropeos.xlsx', sheet_name='europa', index=False)
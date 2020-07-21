# receta 5-6 importar archivo excel 

import pandas as pd 

#sheet_name hace referencia a la hoja del archivo
df = pd.read_excel('paisesEur.xlsx', sheet_name='suramerica')

print(df.head())
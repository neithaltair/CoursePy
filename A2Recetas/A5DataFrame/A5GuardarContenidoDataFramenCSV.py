# Pasar contenido de un data frame a csv
#El ejecutarlo crea el archivo paisesEur.csv
import pandas as pd 

paisesEur = ['francia','spain','rusia','portugal','Uk']

paisesEu = pd.DataFrame(data={'pais':paisesEur})

paisesEu.to_csv('paisesEur.csv', index=False)
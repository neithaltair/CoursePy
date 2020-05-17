#Indices
import pandas as pd

lista_valores = [1,2,3]
lista_indices = ['a','b','c']

serie = pd.Series(lista_valores, index=lista_indices)

print(serie)

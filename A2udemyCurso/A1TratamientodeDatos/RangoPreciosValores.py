import pandas as pd
import numpy as np

precios = [42,11,25,45,35,58,75,65,85,98,23]
rangoPrecios = [10,20,30,40,50,60,70,80,90,100]

preciosConRango = pd.cut(precios, rangoPrecios)
print("\nRango de los precios asignados\n",preciosConRango)

#contar cuantos hay en cada categoria
print(pd.value_counts(preciosConRango))
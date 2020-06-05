#Histogramas
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib as mpl


datos1 = np.random.randn(100)
print(datos1)

#REPRESENTA DATOS 1
mpl.pyplot.hist(datos1)
#mpl.pyplot.show()

#REPRESENTA DATOS 2
datos2 = np.random.randn(80)
mpl.pyplot.hist(datos2)

#REPRESENTA LOS DOS DATOS
mpl.pyplot.hist(datos1, color='green', alpha=0.3, bins=20, density=True)
mpl.pyplot.hist(datos2, color='blue', alpha=0.3, bins=20, density=True)
mpl.pyplot.show()

#COMPROBAR SI CADA UNO DE LOS ELEMENTOS DE UN ARREGLO SON VALORES FINITOS O
#DISTINTOS DE np.nan o np.inf

import numpy as np

a = [0,1,2, np.nan, np.inf, -np.inf]

#Metodo isfinite
#Comprueba elemento a elemento el contenido de una arreglo
print("\nImprime que valores son finitos\n",a,"\n",np.isfinite(a))
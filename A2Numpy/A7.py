#COMPROBAR SI CADA UNO DE LOS ELEMENTOS DE UN ARREGLO ES NULO ('np.nan')

import numpy as np

a = np.array([2,54,5,98, np.nan, 564, 84, np.nan])

#np.isnan evalua elemento a elemento si son nulos.
print("\nEvalua si elementos son nulos\n",a,"\n",np.isnan(a))
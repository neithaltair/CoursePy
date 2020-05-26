#COMPROBAR SI LOS ELEMENTOS DE UNA ARREGLO SON INFINITOS (POSITIVO O NEGATIVO)
import numpy as np

a = np.array([0,1,2, np.inf, -np.inf])

#Funcion isinf comprueba si son infinitos positivos o inf negativo
print("\nComprueba si son infinitos pos o neg\n",a,"\n",np.isinf(a))
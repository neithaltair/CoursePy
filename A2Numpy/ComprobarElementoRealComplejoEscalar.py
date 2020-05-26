#COMPROBAR SI CADA ELEMENTO DE UN ARREGLO NUMPY ES UN REAL, COMPLEJO O ESCALAR

import numpy as np
a = np.array([1,2, 1+3j, 3, 2j])

#PARA COMPROBAR SI TIENE NUMEROS COMPLEJOS np.iscomplex()
print("\nImprime si con complejos\n",a,"\n",np.iscomplex(a))

#PARA COMPROBAR SI ES REAL np.isreal()
print("\nImprime si es real\n",a,"\n",np.isreal(a))


#PARA COMPROBAR SI ES ESCALAR np.isscalar()
#para verificar si es escalar se pasa un numero no un arreglo
b = 5.5
print("\nImprime si es scalar\n",b,"\n",np.isscalar(b))

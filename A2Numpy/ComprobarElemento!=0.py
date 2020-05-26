#Comprobar si en un arreglo existe al menos un elemento distinto de cero
import numpy as np

a = np.array([0,0,1,0])

#Comprobar si al menos un elemento es distinto de cero
#Imprime true si al menos uno es distinto
print("\nComprueba si un elemento es distinto a cero\n",a,np.any(a))

a [2] = 0

#Retorna False si ningun elemento es distinto a cero
print("\nEvalua el nuevo valor en el arreglo\n",a,np.any(a))

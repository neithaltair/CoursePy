import numpy as np

a = [1,2,3,4,5,6,7,8]

#Con la funcion all nos retorna si en la matriz hay un 0
#Retorna true si no hay ceros
print("Matriz que evalua\n",a,np.all(a))

#Cambiando valor en matriz
#Retorna false si tiene ceros
a [2] = 0
print("\nMatriz con cero\n",a,np.all(a))


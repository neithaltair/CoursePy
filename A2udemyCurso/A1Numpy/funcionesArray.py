import numpy as np


array = np.arange(5)

#Sacar raiz al contenido del array
print("Raiz de los numeros = ",np.sqrt(array))

#Crecion de numeros aleatorios
print("Numeros aleatorios = ",np.random.rand(5))

#Suma de los array
array = ([1,2,3,4,5,6])

array1 = ([10,20,30,40,50,60])

print("Suma de los array = ",np.add(array,array1))

#Calcular cual de los array son los mayores
print("El numero mayor = ",np.maximum(array1,array))
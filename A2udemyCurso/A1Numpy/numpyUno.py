import numpy as np

print(np.zeros(4))
print(np.ones(5))

print(np.arange(5))

#Se puede almacenar en una variable
a = np.arange(6)
print(a)
#Se puede recorrer el array con un for
for i in a:
    print(i)

#Se puede usar el range con saltos
print(np.arange(2,20,3))


#A partir de una lista se puede hacer la creacion del array
lista0 = [1,2,3,4,5,6,7,8,9]
array = np.array(lista0)

print(array)


#Se puede hacer la creacion de un array doble
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

lista_doble = (lista1,lista2)

arraydoble = np.array(lista_doble)

print(lista_doble)

#se puede observar el contenido del array, el orden
print(arraydoble.shape)
print(arraydoble.dtype)
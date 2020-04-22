#Crear la funcion "pares" que devuelva una array de numeros pares entre dos valores pasados
#como parametros a la funcion (inicio y fin)
#Utilizar la funcion "pares" con los numeros 1 y 30
#Utilizar la funcion "pares" con los numeros 2 y 40
import numpy as np

x = int(input("El primer valor ="))
y = int(input("El segundo valor ="))

#El array sera igual a un array que contenga un rango
#de valores entre x y y de dos en dos
array = np.array(np.arange(x,y))

#recorrer el array
for i in array:
    #si el numero del array es par
    if (i%2==0):
        #Almacena los numeros en el array
        array1 = np.array(i)
        #imprime el array
        print(array1)


import numpy as np

array1 = np.array([1,2,3,4])

print(array1)

#Se pueden ejecutar sumas a los numeros del array

print("Sumados por  4 = ",(array1 + 4))

#Se pueden multiplicar

print("Multiplicados = ",(array1 * 9))


#Se pueden dividir

print("Division = ",(array1 / 2))

#Se pueden elevar a una potencia

print("Potecnia 4 =",(array1 **4))


#SE PUEDEN REALIZAR OPERACIONES CON LOS ARRAY DOBLES

lista1 =[20,21,25,48,97,56,21]
lista2 =[50,87,98,96,41,58,98]
listadoble = (lista1,lista2)
arraydoble = np.array(listadoble)

print(arraydoble)
print(arraydoble.shape)

#Operaciones para el array doble
print("Array doble multiplicado = \n",arraydoble*50)

print("\nArray doble dividido = \n",arraydoble/2)

print("\nArray doble sumado = \n",arraydoble+2000)

print("\nArray doble restado = \n",arraydoble-50)



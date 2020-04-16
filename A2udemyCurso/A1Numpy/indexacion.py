import numpy as np

#se genera un array de 0 hasta 100
array = np.arange(0,100)
print(array)

#se puede generar un subconjunto del array
primeros = array[0:30]
print("\nLos treinta primeros numeros",primeros)

#Numeros medios
middlenumb = array[25:75]
print("\nNumeros medios = ",middlenumb)

#ensenia el array completo
completo = array[:]
print("\nArray completo = ",completo)

#Copia de un array
arrayCopia = array.copy()
print("\nARRAY COPIA",arrayCopia)

#Array de multiples dimensiones
array1 = np.array(([20,30,40],[50,60,70],[80,90,100]))
print("Multiples dimensiones = ",array1)

#ingresar a un valor especifico de un array de varias dimensiones
print("Fila 3 columna 3 = ",array1[2][2])

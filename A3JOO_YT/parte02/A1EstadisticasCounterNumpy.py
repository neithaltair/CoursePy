#ESTADISTICA CON COUNTER Y NUMPY
from collections import Counter
import numpy as np
from scipy import stats

#Counter permite saber que cantidad de veces se repite una letra
listaLetras = ['t', 'u', 't', 't', 'u', 't', 't', 'u', 't']

contador = Counter(listaLetras)
print(contador)

print()

#Mas usos del Counter()
dictLetras = {'t':3, 'u':1, 'w':2, 'x':2, 'y':2, 'z':1}
contador=Counter(dictLetras)
print(contador)

print()

contador = Counter(t=3, u=1, w=2, x=2, z=1)
print(contador)

print()

cadena = 'neithaltairmachucabernal'
contador = Counter(cadena)
print(contador)

print()

#31
#Varias operaciones interesantes de un Objeto Counter
#Numero de ocurrencias de la a en la variable contador referente a cadena
print(contador['a'])
print(contador)

#Realiza la impresion del top 3 de las letras mas comunes en la variable
print("\n", contador.most_common(3))

print()
#OPERACIONES DE ITERACION
for k, v in contador.most_common():
    print("Llave: {} - Valor: {}".format(k, v))

print()

#Realizar la iteracion en una sola linea, SOLO IMPRIME LA CANTIDAD DE VECES
#QUE SE REPITEN LAS LETRAS PERON NO MUESTRA CUALES LETRAS
conteos = [v for k, v in contador.most_common()]
print(len(conteos))
print(conteos)


#OPERACIONES ESTADISCTICAS BASICAS
#CALCULAR PROMEDIO DE LOS CONTEOS

promedio = np.mean(conteos)
media = np.median(conteos)
minimo = np.min(conteos)
maximo = np.max(conteos)

print('Promedio: %f' % promedio)
print('Mediana %f' % media)
print('Minimo %f' % minimo)
print('Max %f' % maximo)

print()

#Calculo de moda de los valores de una lista con el modulo SCIPY
moda = stats.mode(conteos)
print('Moda: {}'.format(moda.mode[0]))
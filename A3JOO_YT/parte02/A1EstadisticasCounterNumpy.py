#ESTADISTICA CON COUNTER Y NUMPY
from collections import Counter
import numpy as pd

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
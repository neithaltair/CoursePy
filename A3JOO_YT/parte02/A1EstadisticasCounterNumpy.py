#ESTADISTICA CON COUNTER Y NUMPY
from collections import Counter
import numpy as pd

#Counter permite saber que cantidad de veces se repite una letra
listaLetras = ['t', 'u', 't', 't', 'u', 't', 't', 'u', 't']

contador = Counter(listaLetras)
print(contador)

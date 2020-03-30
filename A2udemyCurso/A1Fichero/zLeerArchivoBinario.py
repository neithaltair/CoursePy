#pickle - Modulo para leer datos de un archivo binario

import pickle

fichero = open("fichero_colores.pckl","rb")

lista_leida = pickle.load(fichero)

print(lista_leida)
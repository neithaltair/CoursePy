#pickle - Modulo para grabar ficheros binarios

import pickle

lista_colore = {"amarillo","azul","Rojo", "Negro", "Blanco"}

fichero = open("fichero_colores.pckl","wb")
pickle.dump(lista_colore,fichero)

fichero.close()
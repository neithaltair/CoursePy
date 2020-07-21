# Receta 4-8: Guardar datos como objetos

import pickle

#paises = {'colombia':'bogota', 'argentina':'Buenos aires', 'Peru':'Lima'}

#archivoPaises = open('paises.pickle','wb')
#pickle.dump(paises, archivoPaises)

archivo = open('paises.pickle', 'rb')
paisesRecuperados = pickle.load(archivo)

print(paisesRecuperados)
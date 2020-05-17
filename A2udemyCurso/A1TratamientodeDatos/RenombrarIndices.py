#RenombrarIndices
import pandas as pd
import numpy as np
#Creacion de la lista de valores
listaVlr = np.arange(9).reshape(3,3)
print(listaVlr)

listaIndex = list('xyz')
print(listaIndex)

dataFrame = pd.DataFrame(listaVlr, index=listaIndex)
print("\nRealiza la impresion del dataFrame\n",dataFrame)

#Cambiar los indices a mayusculas
#opcion1
newIndex= dataFrame.index.map(str.upper)
dataFrame.index = newIndex

print("\nImpresion de los indez en mayuscula\n",dataFrame)

#Opcioon2
dataFrame = dataFrame.rename(index=str.lower)
print("\nImpresion de los indez en minuscula\n",dataFrame)


#CAMBIAR LOS INDICES
nuevosIndices = {'x':'n','y':'e','z':'i'}
cambio = dataFrame.rename(index=nuevosIndices)

print("\nImpresion del dataFrame cambiando los index\n",cambio)


#CAMBIAR UN INDICE SIN ASIGNAR
nuevos_indices = {'n':'m'}
print(cambio.rename(index=nuevos_indices, inplace=True))
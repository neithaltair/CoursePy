#Indeces
import pandas as pd

listaValores = [1,2,3]
listaIndices = ['a','b','c']
serie = pd.Series(listaValores, index=listaIndices)

#Los indices no se pueden cambiar,
print(serie)

listNotas = [[7,8,9],[2,6,3],[5,10,9]]
listNombres = ['Antonio','Jose','Ramiro']
listMaterias = ['Mate','Sistemas','Programacion']

dataFrame = pd.DataFrame(listNotas, index=listNombres, columns=listMaterias)
print(dataFrame)

print("\nMuestra las listas normalmente = ",dataFrame.columns)
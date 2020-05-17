import pandas as pd
#pasar diccionario como dataFrame
listaAsignatura=('matematicas','historia','fisica')
listaNotas = [8,9,10]
diccionario = {'Asignaturas':listaAsignatura, 'Notas':listaNotas}

print('\nImprimir diccionario = ',diccionario)

dataFrame_notas = pd.DataFrame(diccionario)

print('\nImprime el DataFrame\n',dataFrame_notas)
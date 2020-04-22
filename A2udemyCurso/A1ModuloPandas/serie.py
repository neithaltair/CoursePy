import pandas as pd


serie1 = pd.Series([3,5,7])
print(serie1)

#Imprime el valor segun la posicion
print("Imprime segun posicion =",serie1[1])

#Ejemplo Asignaturas Strings
asig = ['mate','history','fisica','literatura']
nota = [6,8,9,4]

serieNotasDaniel = pd.Series(nota, index=asig)
print("\nLa nota de Daniel en historia es = ",serieNotasDaniel['history'])

#Notas Mayores a 8
print("Notas superiores a 6 =\n",serieNotasDaniel>=6)

#SE PUEDE AGREGAR UN NOMBRE A LA SERIE
serieNotasDaniel.name = 'NotasDaniel'
print("Agrega un nombre a la serie = ",serieNotasDaniel)

#Se puede anexar un index a la serie
serieNotasDaniel.index.name = 'Asignaturas vistas'
print("\nSe asigna un idex a la serie =\n",serieNotasDaniel)

#Convertir la serie en un diccionario
dictiondaniel = serieNotasDaniel.to_dict()
print("\nConvierte la serie en diccionario =",dictiondaniel)

#Se puede convertir le diccionario en serie
serie = pd.Series(dictiondaniel)
print("\nConvierte diccionario en serie =\n",serie)

#Se pueden sumar las notas de todos los estudiantes de la clase
# serieNotasClase = (serieNotasDaniel + serieNotasDaniela)/2
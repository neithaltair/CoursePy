import pandas as pd

serie = pd.Series([1,2,3,4,5], index=list('abcde'))

print(serie)

#Cambiar un valor en la Serie
print("\nImprime el valor de la serie sin guardar los cambios\n")
print(serie.replace(3,100))


#Para guardar cambios se crea variable nueva o se sobreescribe
serie1 = serie.replace(3,100)
print("\nImprime la serie luego de almacenar los cambios\n",serie1)


#POR MEDIO DE UN DICCIONARIO, VARIOS VALORES
serie1 = serie1.replace({1:545,2:985,4:655,5:215})
print("\nRealiza la impresion asignando los cambios por diccionario\n",serie1)

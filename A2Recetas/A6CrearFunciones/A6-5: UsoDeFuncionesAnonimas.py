# receta python 6-5: Uso de funciones anonimas

#Operador Lambda

numeros = [1,2,3,4,5]

numerosCuadrados = list(map(lambda numero: numero**2, numeros))

print(numerosCuadrados)

elevarCuadrado = lambda numero: numero**2

numerosCuadrados = list(map(elevarCuadrado, numeros))

print(numerosCuadrados)
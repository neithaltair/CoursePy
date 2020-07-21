#Receta 3-3: Filtrar un iterador

numeros = range(10)

print(list(numeros))

#Si el nuemero es par, se agrega
imparesIterador = filter(lambda numero: numero%2, numeros)


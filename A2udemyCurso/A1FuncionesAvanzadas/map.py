#aplicar una funcion a cada uno de los elementos de una lista

def multiplicar(numero):
    return numero * 2

numeros = {2,4,5,6,8,10}

numeros1 = {100,154,5454,2125,45,65,98,15}

# a la variable mapeo le asignamos los resultados de multiplicar y la list de numeros
mapeo = map(multiplicar, numeros)

resultado = list(mapeo)
print(resultado)


# MAP EN LINEA
#se puede hacer en una linea
lista_result = list(map(multiplicar, numeros1))

print(lista_result)

#Funcion Lambda
lista_resulta = list(map(lambda numero1: numero1 * 5, numeros1))
print(lista_resulta)
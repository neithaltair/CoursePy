# Receta python 6-6: Generar funciones especializadas.

def generadorMultiplicador(multiplo):
    return lambda x: x * multiplo

# La funcion y el valor de la variable multiplo es asignada a la variable
duplicador = generadorMultiplicador(2)
print(duplicador(3))
print(duplicador(5))
print(duplicador(7))

# La funcion y el valor de la variable multiplo es asignada a la variable
triplicador = generadorMultiplicador(3)
print(triplicador(3))
print(triplicador(5))
print(triplicador(7))
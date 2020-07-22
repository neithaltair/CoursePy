#Receta python 6-1: Crear una funcion

def calcularCubo(x):
    """
    Calcula el cubo de un numero
    :param x: numero a calcular el cubo
    :return: cubo de un numero
    """
    cubo = x ** 3

    return cubo

print(calcularCubo(8))

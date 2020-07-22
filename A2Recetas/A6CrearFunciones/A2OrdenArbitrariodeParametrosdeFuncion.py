#Receta python 6-2 Orden arbitrario d parametros en una funcion

def calcularCubo(x):
    """
    Calcula el cubo de un numero
    :param x: numero a calcular el cubo
    :return: cubo de un numero
    """
    cubo = x ** 3

    return cubo

#Se pasa de manera explicita el nombre del argumento
print(calcularCubo(x=5))

def multiplicar(a,b,c):
    """
    Multiplica tres numeros
    :param a: num a
    :param b: num b
    :param c: num c
    :return: multiplicacion entre a, b, c
    """
    return a*b*c

print(multiplicar(2,5,7))

#SE especifica que valores les vamos a dar a cada una de las variables
print(multiplicar(a=5,b=2,c=7))

print(multiplicar(a=int(input("ingrese el valor a =")), b=int(input("ingres valor b =")), c=int(input("ingrese valor c ="))))
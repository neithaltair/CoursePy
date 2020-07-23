#Receta python 6-3: Usar valores predeterminados para parametros

#Especificar un valor de un parametro
def calcularPotencia(base, exponente=2):
    """
    Calcula la potencia
    :param base: Base
    :param exponente: Exponente
    :return: Potencia
    """
    return (base*exponente)

print(calcularPotencia(5,4))
print(calcularPotencia(8,9))
print(calcularPotencia(10,800))
print("\n Potencia con parametro por defecto")
#Pueba haciendo uso del parametro por defecto
print(calcularPotencia(5))
print(calcularPotencia(8))
print(calcularPotencia(10))

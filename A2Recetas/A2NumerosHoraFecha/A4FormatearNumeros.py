#Como formatear nuemeros

entero = 52
decimal = 31415.9265
porcentaje = 0.19

#Se solicita que pase el entero a valor hexadecimal
print(format(entero, 'x'))

#Se pueden formatear decimales en notacion cientifica
print(format(decimal, 'E'))

#Formatear decimal para especificar cantidad de decimales
print(format(decimal, '.2f'))

#Imprime el numero en porcentaje
print(format(porcentaje, '%'))

#https://docs.python.org/3.7/library/string.html#formatspec
#https://docs.python.org/3.7/library/functions.html?highlight=format#format

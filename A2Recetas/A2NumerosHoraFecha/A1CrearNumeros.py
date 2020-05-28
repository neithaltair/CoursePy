#Crear numero enteros

#1. literales
#2. Entrada del usuario

entero = 905

#conversion de la cadena de caracteres a entero
numero = int(input('Escriba un numero: '))

print(numero, entero)

#Indica que cantidad de bits ocupa el numero ingresado por el usuario
print('\nIndica cantidad de bits que ocupa\n',numero.bit_length())

#binario
binario = '111'
#Pasar el binario a entero
representacionEntera = int(binario,2)
print("\nRepresentacion entera\n",representacionEntera)

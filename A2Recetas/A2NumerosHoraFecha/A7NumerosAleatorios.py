#Generar numeros aleatorios

import random

#Imprime un numero aleatorio pero no necesariamente entero
print(random.random())

#Genera un numero aleatorio entre 0 y 100
print(random.randint(0,100))

primos = [2,3,5,7]

#Realiza la seleccion al azar de uno de los numeros
print("\nNumero al azar elegido = ",random.choice(primos))
# Las tuplas son mas rapidas, ocupan menos espacio
# formatean strings, pueden utilizarse como claves en un diccionario

# son inmutables, no se pueden modificar despues de su creacion
# permiten extraer porciones pero el resultado es una tupla nueva

# la diferencia con las listas es que va en parentesis y no corchetes aunque puede ir sin ellos
# a la hora de acceder a los elementos de una tupla inician con indice en posicion cero

miTupla=("Hola","This","is","a","Tupla","is")

print(miTupla[2])

# para convertir una tupla en lista 
miLista = list(miTupla)

print(miLista[:])

#para convertir una lista en una tupla
miTupla1 = tuple(miLista)

print(miTupla1[:])

# Buscar si un elemento hace parte de la tupla
print("This" in miTupla1)

# cuantas veces esta un elemento en la tupla
print(miTupla1.count("is"))

#Saber la longitud de la tupla, cuantos elementos tiene
print(len(miTupla1))

#Funciona de la misma forma jpara saber la longitud de las listas
print(len(miLista))

# Desempaquetado de tupla: Permite asignar los elementos de la tupla a 
# diferentes variables

miTupla2 = ("hola",5,6,54,54878)
saludo, num1, num2, num3, num4 = miTupla2

print(saludo)
print(num4)
print(num2)
print(num3)
print(num1)



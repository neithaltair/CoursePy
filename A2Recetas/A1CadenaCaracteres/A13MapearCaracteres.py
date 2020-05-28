#Mapear cadena de caracteres de un objeto String

lenguaje = 'pithon'
print(lenguaje)

print(lenguaje.replace('i', 'y'))

#El uso del mapeo sirve para cambiar uno a uno los elementos de un caracter
mapa = lenguaje.maketrans('ito', 'oti')
print(lenguaje.translate(mapa))

lenguaje = 'Pyt         hon'
print(lenguaje)
#Quitar los espacios en blanco
lenguaje = lenguaje.translate(str.maketrans({' ': None}))

print(lenguaje)

from websocket._http import proxy_info

lenguaje = 'python es genial'

print('tamano\n',len(lenguaje))

#Saber posicion de atras hacia adelante
print('\nposicion inversa\n',lenguaje[-5])

#Extraer subcadena
print('\nsubcadena\n',lenguaje[0:6])

#Extraer subcadena si no se sabe posicion con find
print('\nPosicion de la letra e en la cadena\n',lenguaje.find("e"))

#Extraccion de la palabra es de la cadena
print('\nExtraer la palabra es\n', lenguaje[7:9])

#Extraccion de la subcadena con busqueda incluida .find
# desde la posicion cero hasta el indice de la s +1 para que no excluya la S
print('\nExtraer inicio de la cadena\n', lenguaje[0:lenguaje.find("s") + 1])

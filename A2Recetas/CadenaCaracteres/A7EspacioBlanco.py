#Remover espacacio u otro caracter de una cadena de caracteres

lenguaje = 'python es genial'

print('Impresion de la cadena con espacios.\n',lenguaje)
#Funcion en la clase string
print('\n',lenguaje.strip())

#Eliminar un caracter especifico
a = 'xxxyyyxxx'
print('\n',a.strip('x'))

#Caracteres a la derecha o izquierda lstrip(), rstrip()
print('\nQuitando izquierda\n',a.lstrip('x'))
print('\nQuitando derecha\n',a.rstrip('x'))

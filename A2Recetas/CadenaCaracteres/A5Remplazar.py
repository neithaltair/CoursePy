#Remplazar texto en una cadena de caracteres:

frase = 'python.com es el sitio oficial de python'

#Remplazar de forma manual:
fraseCorregida = frase[0:7] + 'org' + frase[10:]

print("Frase corregida de forma manual\n",fraseCorregida)


#Forma automatica: uso del metodo replace
fraseCorregida = frase.replace('com', 'org')
print('\nFrase corregida de manera automatica\n',fraseCorregida)
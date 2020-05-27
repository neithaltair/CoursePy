#Invertir una cadena de caracteres

#Slice notation: que sirve para obtener subcadenas de caracteres

#[x:y:z] el z indica los saltos

frase = 'Python es una lenguaje de progrmacion'

#Se pueden realizar saltos positivos de la subcadena (positivos = 2)
print("\nImprime valores positivos\n",frase[0:6:2])

frase = frase.replace("una",'un')

#Obtener la cadena invertida
print("\nImprime la cadena invertida\n",frase[::-1])



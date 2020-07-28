numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(type(numeros))
print(len(numeros))
print(numeros)

print()

paresTriplicados = []

for n in numeros:
    if n % 2 == 0:
        paresTriplicados.append(n * 3)

print(type(paresTriplicados))
print(len(paresTriplicados))
print(paresTriplicados)

print()

#LISTA DE COMPRENSION, Realizar un for en una sola linea
paresTriplicados = [n * 5 for n in numeros if n % 2 == 0]

print(type(paresTriplicados))
print(len(paresTriplicados))
print(paresTriplicados)

print()

#Solucion con ciclos for(iterativa)
num1 = [2, 3, 5, 7, 11]
num2 = [2, 7, 13, 19, 23, 3]
interseccion = []

#Se recorren los dos arreglos, un numero por cada elemento en el
#otro arreglo
for n1 in num1:
    for n2 in num2:
        #Si al recorrer los arreglos, algun elemento esta
        #presente en los dos y no esta en interseccion
        if n1 == n2 and n1 not in interseccion:
            #agregar el numero a la interserccion
            interseccion.append(n1)

print(len(interseccion))
print(interseccion)

#CURSO-28: SOLUCION CON LISTAS DE COMPRENSION PARA HALLAR LA INTERSECCION
# DE DOS LISTAS
print()
interseccion = []
#En la variable resultado se realizara la ejecucion en una sola linea
resultado = [n1 for n2 in num2 for n1 in num1 if n1 == n2 and n1 not in interseccion ]

print(len(resultado))
print(resultado)

#Hallar la interseccion de dos conjuntos (grupos)
resultado = set(num1) & set(num2)
print("\n",len(resultado))
print("Haciendo uso del set ",resultado)

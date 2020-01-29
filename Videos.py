mensaje = """ Esto es un mensaje 
con tres 
saltos de linea"""

#se hace el uso de las comillas para poder imprimir con saltos de linea.

print(mensaje)





#uso del condicional if 
numero1 = 5
numero2 = 7

if numero1>numero2:
	print("El numero 1 es mayor")
else:
	print("El numero 2 es mayor")





#Uso de las funciones en python

def mensaje():

	print("a")
	print("b")
	print("c")

mensaje()


#6-79
#uso de las funciones con operaciones y cambiando los parametros
def suma(num1, num2):

	print(num1+num2)


suma(20,30)

suma(50,50)

suma(1039,60435)


#Uso de la funcion con return

def suma(num3,num4):

	res = num3+num4
	return res

ResSum1 = suma(1,2)

print(ResSum1)


#7-79
#que son las listas en python
# guarda diferente tipo de valores y se expande de manera dinamica


miLista = ["Falca","Jeims","Fred","Meb"]
# Si se desea acceder a una posicion en especifico se coloca el numero
# y retorna el contenido de esa posicion
print(miLista[:])

# Acceder a una posicion en especifico
print(miLista[3])

# Acceder a una porcion de la lista 
print(miLista[0:3])

# Se puede hacer omision de el cero y python entendera que debe hacer
print(miLista[:2])

# Desde una posicion hasta el final
print(miLista[0:])

# Con la funcion append agrega el objeto como ultimo en  la lista
miLista.append("Neith")

# Con la funcion insert  se puede indicar en que posicion colocar el elemento nuevo
miLista.insert(2,"Altair")

print(miLista[:])

#Si se quieren añadir varios elementos al tiempo se usa extend
miLista.extend(["Sol","Jaime","Gabriel"])

print(miLista[:])

# Para saber la posicion en la que se encuentra un elemento se utiliza index
print(miLista.index("Altair"))

# Anexando numeros a la lista
miLista.append(7)

# Anexando diferente tipos a la lista
miLista.extend([8457.65, True, 45])

print(miLista[:])

# Eliminacion de elementos de una lista
miLista.remove("Jaime")
# para eliminar enteros o demas se debe hacer sin comillas
miLista.remove(7)

#Eliminar el ultimo elemento de una lista
miLista.pop()

print(miLista[:])

# Se pueden unir dos listas con operador matematico logrando una tercera
# lista con la union de las dos anteriores 
miLista2 = ["Contenido","nuevo","para la lista"]

miLista3 = miLista + miLista2

print(miLista3[:])

# Se puede utilizar un tipo de multiplicacion para que 
# el codigo haga la impresion multiple

print(miLista[:] * 2)
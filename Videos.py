mensaje = """ Esto es un mensaje 
con tres 
saltos de linea"""

#se hace el uso de las comillas para poder imprimir con saltos de linea.

print(mensaje)





#uso del condicional if 
numero1= 5
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




#Receta 3-2 : extraer el ocontenido de un iterador

#enumerate 

lenguajes = ["python","java","c#","php","c++"]

enumerador_lenguajes = enumerate(lenguajes)

print(next(enumerador_lenguajes))

#Para iniciar la lista desde una posicion especifica 
#Se crea una nueva varibale que empezara desde la posicion 5
enumerador_lenguajes2 = enumerate(lenguajes,5)

#Se imprime el contenido desde la posicion 5
print(next(enumerador_lenguajes2))
print(next(enumerador_lenguajes2))
print(next(enumerador_lenguajes2))

#hacer un ciclo for que muestra la posicion de los elementos
for indice, elemento in enumerate(lenguajes):
	print(indice, elemento)
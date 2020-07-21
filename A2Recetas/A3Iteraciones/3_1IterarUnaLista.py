#Receta 3-1: Iterar una lista 

primos = [2,3,5,7,11]

for primo in primos:
	print(primo)

#Iterar de forma "manual"
iterador = iter(primos)
#Imprime una a una las iteraciones 
print(next(iterador))

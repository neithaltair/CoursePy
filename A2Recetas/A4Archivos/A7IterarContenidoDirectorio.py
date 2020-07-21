#Iterar contenido de un directorio

#MODULO INCORPORADO POR DEFECTO
import pathlib

p = pathlib.Path('.')

for elemento in p.iterdir():
	print(elemento)

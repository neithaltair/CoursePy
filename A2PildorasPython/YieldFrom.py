def retorna_ciudades(*ciudades):
    for elemento in ciudades:

        #Si se quita el from del yield imprimira las ciudades completas
        #con el yield from se hace impresion de las letras de cada una de 
        # las ciudades
        yield from elemento


ciudades_devueltas = retorna_ciudades("Bogota","Medellin","Cali","Cartagena")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
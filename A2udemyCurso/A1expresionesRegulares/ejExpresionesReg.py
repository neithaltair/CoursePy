#Crear una funcion buscar que mediante una expresion regular indique si una palabra esta en una frase

#probar la funcion de "buscar" con estas frases
#texto = Esto es una frase de pruebas para hacer busquedas

#palabra a buscar = 'frase'
# en caso de encontrar la palabra en la frase, indicar en que posicion empieza y en cual finaliza
import re

texto = "Esto es una frase de pruebas para hacer busquedas"


def buscar():
    busqueda = re.search(input("Palabra a buscar en texto = "),texto)

    if(busqueda):
        print(busqueda)
        inicial = busqueda.start()
        final = busqueda.end()
        print("Inicia en la posicion {}, y termina en la posicion {}".format(inicial, final))
    else:
        print("no match found")



buscar()


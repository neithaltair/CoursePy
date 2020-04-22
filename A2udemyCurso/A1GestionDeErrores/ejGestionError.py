#Crear la funcion "operacion" que dados 3 numeros, divida el primer numero entre la resta de los otrso dos numeros

#Utilizar la funcion creada con los numeros 5,4,2
#utilizar la funcion creada con los numeros 6,3,3

#utilizar el bloque try ... except para controlar cualquier posible error

def operacion(x,y,z):

    try:
        dividir = x / (y-z)
        print(dividir)
    except:
        print("Error en la operacion")



operacion(5,4,2)
operacion(6,3,3)
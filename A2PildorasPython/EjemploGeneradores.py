#Definicion de la funcion 

def pares (limite):
    index = 10
    #En este caso definimos un bucle finito, finalizando en el limite
    while index <= limite:
        #Establecemos de cuanto en cuanto ira el programa
        yield index*2
        
        index = index+1

devuelvePares = pares(20)

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

# El for sirve para imprimir todos los numeros de una sola vez
#for i in pares():
#    print (i)
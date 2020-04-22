range(0,11)

for numero in range (0,11):
    print(numero)

#FUNCION PARES
def pares(maximo):
    for numero in range(maximo):
        if(numero%2==0):
            #Funcion generadora usa yield
            yield numero

maximo = 30
for numero in pares(maximo):
    print(numero)
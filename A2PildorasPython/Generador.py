def generarPares(limite):

    num = 1

    while num<limite:
        yield num*5

        num+=1

devuelvePares = generarPares(10)

for i in devuelvePares:
    print(i)


#Video 19 pildoras informaticas

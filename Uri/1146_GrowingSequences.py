#Continues inicia en True
continues = True

#Mientras la variable continues sea igual a true
while continues == True:
    
    #Leera el entero x 
    x = int(input(""))

    #SI x es igual a 0 la variable continues pasara a False
    if x==0:
        continues = False

    #se imprimiran los numeros de 1 en 1 hasta X+1
    for number in range(1,x+1):

        #Se establece la forma en la que se imprimiran, la cual sera en linea
        print(number, end=" ")

    #Se hace print para que haga el salto de linea normal para asi mantener el orden
    print("")


    

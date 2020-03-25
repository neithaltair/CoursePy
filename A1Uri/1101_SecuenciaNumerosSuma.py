m = int(input("Num 1 = "))
n = int(input("Num 2 = "))
suma = 0 
if m<n:
    number = m

    while number <= n:

        suma += number

        print(number, end=" ")

        number+=1

    print("Suma = ",suma)
        
        



elif n<m:
    # la variable number toma el valor de n 
    number = n

    #mientras number sea menor igual que m 
    while number <= m:
        
        #la variable suma "sumara" los valores de number empezando en 2
        suma += number

        #imprime el valor de number estableciendo cuales son los numeros que se suman
        #print("valor number = ",number)

        #imprime el valor de number en linea separado por un espacio
        print(number, end=" ")

        #contador que aumenta de uno en uno cada que se imprime number
        number+=1
        
    # imprime el valor de la suma total 
    print(" Sum=",suma)  
    


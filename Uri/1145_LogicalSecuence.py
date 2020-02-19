x = int(input("x = "))
y = int(input("y = "))
z=1

#Mientras z sea menor igual que y
while z<=y:

    #Imprima z, seguido de un espacio
    print(z, end=" ")

    #Si z modulado en el numero x es igual a 0 significa que es multiplo
    # lo cual hace que haga un salto de linea 
    if z%x ==0 :
        print("\n")
    
    #incrementa el valor de z
    z+=1
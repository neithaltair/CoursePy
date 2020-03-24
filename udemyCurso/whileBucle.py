#WHILE
print("uso del bucle while")
valor = 1
fin = 10
while(valor < fin):
    print(valor)
    valor +=1

#se para en el numero 4 BREAK
print('\n Imprime while con break terminando en el 5')
valor1 = 1
while(valor1<fin):
    print(valor1)
    valor1+=1
    if(valor1 == 5):
        break

#Se salta uno de los numeros CONTINUE
print("\n Imprime while saltando un numero")
valor2 = 0
while(valor2<fin):
    valor2+=1
    if(valor2 == 6):
        continue
    print(valor2)



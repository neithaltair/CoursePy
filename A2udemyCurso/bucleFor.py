#Imprimir los colores uno por uno
colores = ['amarillo', 'azul','rojo','yellow','blue','red']
for i in colores:
    print(i)

# imprimir caracter por caracter
print("\n")
cadena = "Vas a ser mi perra"
for caracter in cadena:
    print(caracter)

#Imprimir una lista de numeros con range
print("\n")
range(0,8)
for numero in range (8):
    print(numero)

# empezar los numeros en el 3 hasta el 8
print("\n")
for numero1 in range (3,8):
    print("numeros desde 3 a 8 = ",numero1)

print("impresion de los numeros usando break")
# imprimir numeros de dos en dos
print("\nImpresion de numeros de dos en dos")
for numero2 in range(4,20,2):
    print(numero2)

print("\n")
#Break PARA PARA EL BUCLE
for numero3 in range (10):
    if(numero3 == 5):
        break
    print(numero3)

print("\n")
#CONTINUE PARA PARAR SOLO LA ITERACION ACTUAL SE SALTA UNO DE LOS NUMEROS
print("Impresion haciendo uso del continue, no imprime el seis")
for numero4 in range(10):
    if(numero4 == 6):
        continue
    print(numero4)

print('\n')
#FOR DOBLE
print("impresion del for doble")
for numero5 in range (10):
    for numero6 in range(5):
        print(numero5, numero6)


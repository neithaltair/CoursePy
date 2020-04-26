import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero = "))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un negativo")

    if intentos > 2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;

    numero=int(input("Introduce un numero: "))
    if numero<0:
        intentos += 1

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de ", numero, "es", solucion)

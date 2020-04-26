i=1

while i<=10:
    print("Ejecucion "+str(i))
    # El contador no funciona con ++, funciona con +=1  o variable = variable + 5 
    i+=1

print("Termino la ejecucion")


edad = int(input("Ingrese edad mayor a 0 = "))

while edad < 0:
    edad=int(input("Ingrese la edad correcta = "))

print("Correcto")
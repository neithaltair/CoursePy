#Es importante siempre identificar en que linea del codigo el script arroja el error
# se hace uso de un while True, que hara infinito el bucle
# se usa el break para que salga del bucle una vez el programa reciba los valores adecuados 
# En el except se establece que tipo de error se saltara y enviara un mensaje al usuario.

def multiplica (num1,num2):
    return num1*num2

def divide (num1,num2):
    try:
        return num1/num2

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operacion erronea"

while True:    
    try: 
        op1 = (int(input("Introduce el primer numero : ")))

        op2 = (int(input("Introduce el segundo numero : ")))

        break
    
    except ValueError:
        print("Los valores ingresados no son validos")

operacion = input("multi, divide : ")

if operacion == "multi":
    print(multiplica(op1,op2))

elif operacion == "divide" : 
    print(divide(op1, op2))

else:  
    print("Operacion no completada")


print("Operacion ejecutada. ")
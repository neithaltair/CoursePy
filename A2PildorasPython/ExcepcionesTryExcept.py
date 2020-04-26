def multiplica (num1,num2):
    return num1*num2

def divide (num1,num2):
    try:
        return num1/num2

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operacion erronea"
    

op1 = (int(input("Introduce el primer numero : ")))

op2 = (int(input("Introduce el segundo numero : ")))

operacion = input("multi, divide : ")

if operacion == "multi":
    print(multiplica(op1,op2))

elif operacion == "divide" : 
    print(divide(op1, op2))

else:  
    print("Operacion no completada")


print("Operacion ejecutada. ")
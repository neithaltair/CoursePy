def divide():
    
    while True:
        try:
            op1 = (float(input("Introduce el primer numero = ")))
            op2 = (float(input("Introduce le segundo numero = ")))


            print("la division es : " , op1/op2)

            break

        except ValueError: 
            print("Solo ingresar numeros")

        
        except ZeroDivisionError:
            print("No se puede hacer una division en 0")


    print("Calculo finalizado")

divide()
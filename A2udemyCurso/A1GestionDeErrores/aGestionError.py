# try.....catch..... else .... finally

num1 = 10
num2 = 0

#En el try va lo que puede producir el error
try:
    res = num1/num2
    print(res)

#se puede agregar mas de un except
except ZeroDivisionError:
    print("Error de Division Cero")

# se puede hacer uso del except, sin especificar el tipo de error que capturara
except:
    print("Error de division")


#se puede hacer implementacion de un else
else:
    print('La division funciona correctamente')

#finally permite imprimir codigo independiente a los resultados de try y except
finally:
    print('Siempre imprime')

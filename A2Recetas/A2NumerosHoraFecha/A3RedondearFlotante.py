#REDONDEAR NUMEROS FLOTANTES A ENTEROS

pi = 3.1415

#1. int() Utilizar la funcion
#2. trunc() del paquete math
#3. round()

print(type(pi))#1
ente = int(pi)#1
print("\nNumero redondeado con int\n",ente)#1

from math import trunc
print()#2
print('Numero redondeado con trunc\n',trunc(pi))#2

print()#3
print("\nNumero redondeado con round\n",round(pi))#3
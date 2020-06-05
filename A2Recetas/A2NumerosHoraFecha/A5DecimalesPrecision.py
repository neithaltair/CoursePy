#Decimales con precision arbitraria

from decimal import *

print(getcontext())

print(Decimal(1)/Decimal(3))


#Permite realizar un enfasis en la cantidad de numeros a imprimir
getcontext().prec = 3
print(Decimal(1)/Decimal(3))


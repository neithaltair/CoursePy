#Conversion de hexadecimal a bytes
test = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
#Se asigna a la variable el valor en bytes de los hexadecimal
new_test = bytes.fromhex(test)
#Imprime el valor en bytes
print(new_test)
#Se hace la importacion del modulo pybase64
import pybase64

# informacion sobre base 64 https://programacion.net/articulo/codificar_y_decodificar_en_base64_con_python_1385
test = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

#Pasa el contenido del hexadecimal a bytes
bites = bytes.fromhex(test)

#Impresion de los bytes
#print(bites)

#Se codificaran los bytes en base64
encode_64 = pybase64.b64encode(bites)
# Impresion de los bytes codificados
print(encode_64)
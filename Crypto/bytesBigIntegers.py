#Se importa el modulo crypto
#La idea es convertir 
#el mensaje -> bytes ascii -> bytes hexadecimales-> base64 -> base 10
#y revertir el proceso, para realizar esto se implementra el modulo pycryptdome
#y las funciones  bytes_to_long --y-- long_to_bytes
import Crypto
#Se asigna el numero a decodificar en la variable valor 
valor = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#Se hace uso de len() para identificar la cantidad de caracteres que tiene la variable valor
cantidad = len(str(valor))

solucion = valor.to_bytes(cantidad, 'big'); print(solucion)
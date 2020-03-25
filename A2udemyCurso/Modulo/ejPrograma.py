# CREAR UN MODULO "MOD1.PY"
# AGREGAR LA CLASE "COCHE" CREADA EN EL EJERCICIO ANTERIOR EN MODULO 1
# ANADIR LA FUNCION LAMBDA "MEDIA" CREADA ANTERIORMENTE EN MODULO 1

# CREAR UN PROGRAMA EN PYTHON PROGRAMA1
# IMPORTAR EL MODULO "MODULO1" ANTES CREADO
# CREAR UN OBJETO "COCHE1" AL INSTANCIAR LA CLASE "COCHE"
# MEDIANTE PRINT MOSTRAR LAS CARACTERISTICAS DEL COCHE
# CALCULAR LA MEDIA DE 3 NOTAS Y MOSTRAR EL RESULTADO CON PRINT

#EJECUTAR EL PROGRAMA "PROGRAMA.PY" Y VER EL RESULTADO

import ejModulo1

# se instancia el coche1 con modulo y clase coche
coche1 = ejModulo1.coche("a","b","c","d")
# luego de instanciar el coche1 mostrar las  caracteristicas
coche1.mostrarCaracteristicas()
#______________________________________________________

coche2 = ejModulo1.coche("e","f","g","h")
print(coche2.mostrarCaracteristicas())

#______________________________________________________

#funcion lambda
media = ejModulo1.media(10,10,10)

print("Resultado media = {}".format(media))


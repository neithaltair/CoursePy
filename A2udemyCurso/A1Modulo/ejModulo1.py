#CREAR UN MODULO "MOD1.PY"
#AGREGAR LA CLASE "COCHE" CREADA EN EL EJERCICIO ANTERIOR EN MODULO 1
#ANADIR LA FUNCION LAMBDA "MEDIA" CREADA ANTERIORMENTE EN MODULO 1

#CREAR UN PROGRAMA EN PYTHON PROGRAMA1
#IMPORTAR EL MODULO "MODULO1" ANTES CREADO
# CREAR UN OBJETO "COCHE1" AL INSTANCIAR LA CLASE "COCHE"
#MEDIANTE PRINT MOSTRAR LAS CARACTERISTICAS DEL COCHE
# CALCULAR LA MEDIA DE 3 NOTAS Y MOSTRAR EL RESULTADO CON PRINT

#EJECUTAR EL PROGRAMA "PROGRAMA.PY" Y VER EL RESULTADO

#Se importa la funcion lambda
media = lambda n1, n2, n3: (n1+n2+n3)/3

#Se importa la clase coche
class coche:
    def __init__(self, marca, color, gasolina, cilindrada):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina
        self.cilindrada = cilindrada

    #marca = input("ingrese = ")


    def mostrarCaracteristicas(self):
        print("Marca = {}, Color = {}, Gasolina = {}, Cilindrada = {}".format(self.marca, self.color, self.gasolina, self.cilindrada))


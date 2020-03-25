#Programa que llamara al modulo modulo1.py

import modulo1

#Importa la funcion saludar de modulo1
print("\nImporta la funcion saludar de modulo1")
modulo1.saludar("Neith")

#Le asigna un nuevo valor a la variable nombre
print("\nLe asigna un nuevo valor a la variable nombre")
nombre = "Altair"
modulo1.saludar(nombre)

#Importa la funcion despedir de  modulo1
print("\nImporta la funcion despedir de  modulo1")
modulo1.despedirse("Vemos locas")


#Realiza saludo con variable ingresada en codigo
print("\nRealiza saludo con variable ingresada en codigo")
def saludoDoble (nombre1):
    print("Hola ", nombre1)

print(saludoDoble("Fredy"))


#Realiza saludo con variable ingresada por usuario
print("\nRealiza saludo con variable ingresada por usuario")
print(saludoDoble(input("Nombre2 = ")))
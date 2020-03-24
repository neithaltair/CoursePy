#funciones

def saludar():
    print("Hola a todos")
    print("como estan")
    print("esto es una funcion")


print(saludar())

#FUNCIONES CON VARIABLES
print("\nFuncion con variable")
def saludar1(nombre):
    print("Hola {} como estas".format(nombre))

print(saludar1("Fredy"))


#Funcion sumar
print("\nFuncion sumar")
def sumar(num1,num2):
    print(num1+num2)

print(sumar(5,10))


#PASO DE VALOR POR REFERENCIA
print("\n Paso de valor por referencia")
colores = ["rojo","azul", "amarillo"]

def incluirColor (colores, color):
    colores.append(color)

color = input("Agregue color = ")
incluirColor(colores, color)

print(colores)


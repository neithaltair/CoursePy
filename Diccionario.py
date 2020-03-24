#nombre para el diccionario, siempre va dentro de llaves
miDicccionario={"Colombia":"Bogota", "Argentina":"Buenos Aires", "Chile":"Santiago", "Bolivia":"La Paz", "Ecuador":"Quito"}

#como acceder a un valor en concreto del diccionario
print(miDicccionario["Colombia"])
print(miDicccionario["Ecuador"])

#Anexar una nueva clave al diccionario
miDicccionario["Uruguay"] = "Caracas"

#imprimir todo el diccionario
print("\n",miDicccionario)

#Cambiar el valor de la clave 
miDicccionario["Uruguay"] = "Montevideo"

print("\n",miDicccionario)

#Eliminar elementos del diccionario
del miDicccionario["Chile"]

print("\n Imprime diccionario despues de eliminar a chile = ",miDicccionario)

# Los diccionarios pueden contener todo tipo de 
miDicccionario1 = {23 : "Jordan", "Neymar": 10}

print("\n Los diccionarios pueden contener booleanos, enteros, strings etc = ",miDicccionario1)


#Es posible usar una tupla para asignar las llaves a los valores
miTupla = [1,2,3,4,5,6]
miDicccionario2 = {miTupla[0]:"Keylor", miTupla[1]:"Keylora", miTupla[2]:"Keylorb", miTupla[3]:"Keylorc", miTupla[4]:"Keylord", miTupla[5]:"Keylore"}

print("\n Uso de tupla para la creacion de claves en el diccionario",miDicccionario2)


#Para acceder en un elemento en concreto
print(miDicccionario2[2])


#Crear una tupla dentro de un diccionario
miDicccionario3 = {"Equipo":"Millos", "Estrellas":"15", "Campeonatos":[2012,2016,545,1998,58877,54545]}

print("\n",miDicccionario3)
print("Campeonatos = ", miDicccionario3["Campeonatos"])
print("Equipo = ", miDicccionario3["Equipo"])


#Para imprimir la clave valor se hace uso de item
miDicccionario4 = {"Hola":"1234", "casef":"aaaa"}


#TENER EN CUENTA EL ITEMS Y EL FORMAT PARA IMPRIMIR EL CONTENIDO
for clave,valor in miDicccionario4.items():
    print("{} claves, contenido {}".format(clave, valor))
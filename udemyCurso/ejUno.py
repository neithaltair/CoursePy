diccionario = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

print("Imprime la traduccion de naranja =",diccionario["naranja"])


diccionario["pinia"] = input("Pinia en ingles = ")


print("\nImprime el contenido del diccionario = ")
for frutas in diccionario:
    print(frutas)

#TENER EN CUENTA EL ITEMS Y EL FORMAT PARA IMPRIMIR EL CONTENIDO Y EL NOMRBE DEL DICCIONARIO
print("\nImprime el contenido completo de el diccionario = ")
for clave, valor in diccionario.items():
    print("clave {}, valor {}".format(clave, valor))

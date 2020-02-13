nombreUsuario=input("nombre usuario = ")


print("Nombre es",nombreUsuario.upper())
print("Nombre es",nombreUsuario.lower())
print("Nombre es",nombreUsuario.capitalize())
#print(nombreUsuario.find("@"))

if nombreUsuario.find("@") != 1 and nombreUsuario.count("@") == 1 :
    print("Correo Correcto")
else:
    print("Correo incorrecto")

#Comprobar si se ingresa un numero retorna un booleano 
#TRUE o FALSE 
edad = input("Ingrese edad = ")

print("La edad es : ",edad)
print(edad.isdigit())

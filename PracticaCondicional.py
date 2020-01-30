#print("Verifiacion de edad")

#CONVERTIR LO QUE INGRESA EL USUARIO EN ENTERO DIRECTAMENTE
edad = int(input("Ingresar edad = "))

#if edad >= 18:
#    print("Acceso autorizado")
#elif edad > 100 or edad < 1:
 #   print("Edad incorrecta")
#else:
 #   print("No ingresa")



#uso del condicional in
print("Asignaturas optativas del anio")
print("Asignaturas son = Programacion, Redes, SO, Electronica, Calculo")

#Almacena el valor ingresado por  el usuario
opcion = input("Escribe asignatura escogida = ")

#convierte el valor de la variable a minuscula
asignatura = opcion.lower()

print(asignatura)
# si la materia que ingresa el  usuaario se encuentra dentro de las siguientes
if asignatura in ("programacion", "redes", "so", "electronica", "calculo"):
    # imprime que materia fue seleccionada
    print("La materia seleccionada es = "+asignatura)
else:
    print("La materia no se encuentra en las opciones")
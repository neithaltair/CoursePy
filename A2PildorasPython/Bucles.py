# Bucle for es = for variable in elemento a recorrer : 

for i in [1,1,2,1,1]: 
    
    #Se hace uso del end para establecer como se desea que finalice la impresion, si en la misma linea, con espacio o comas
    print("Imprime", end=", ")


#Ejemplo con un correo 
#correo empieza en falso
email = False
# se pide al usuario ingresar el correo
correo = input("\n \n Ingrese el correo = ")

#si al recorrer correo hay un @ email pasa a True
for i in correo : 
    if i == "@":
        email=True

#Si el email es True, es un correo autorizado
if email == True:
    print("Correo autorizado")
else:
    print("Correo no autorizado\n\n")





# Uso del for con range 
for a in range(30):
    #Se establece la f para que imprima el texto todas las veces que se imprima a
    print(f"El valor de a es = {a}")

# al range se le pueden agregar dos valores mas los que serian hasta que numero va y de cuantos en cuantos va 
print("\n\nImpresion del range del 5 al 50 de 2 en 2")
for n in range (5,50,2):
    print(n)



#USO DEL LEN CON EL FOR 
# for i in range(len(variable)) : 

# para recorrer este for if variable[i] == "a"
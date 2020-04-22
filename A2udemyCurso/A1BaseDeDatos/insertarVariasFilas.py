import _sqlite3

conexion = _sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

#Cantidad de filas que se agregaran
cantidad = int(input("Cuantos valores ingresara = ")); n=1

#Mientras n sea menor a la cantidad por ingresar
while n <= cantidad:
    # Se agregaran a la lista personas el nombre y apellidos
    lista_personas = [(input('Ingrese nombre = '),input('LastName = '),input('Second LastName = '),input('Edad = '))]
    n+=1
    cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

#cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()

conexion.close()
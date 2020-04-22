#CREAR UNA BASE DE DATOS "BASEDATOS.DB"
#CREAR UNA TABLA "PRODUCTOS" CON 3 CAMPOS
#ID = IDENTIFICADOR DEL PRODUCTO DE TIPO NUMERICO
#NOMBRE = NOMBRE DEL PRODUCTO DE TIPO TEXTO
#PRECIO = PRECIO DEL PRODUCTO DE TIPO NUMERICO

#INSERTAR 3 PRODUCTOS EN LA TABLA "PRODUCTOS"
# 1 "IMPRESORA",300
# 2 "RATON",20
# 3 "ORDDENADOR" , 600

#CONSULTAR LOS PRODUCTOS DE LA TABLA "PRODUCTOS"
#CERRAR LA BASE DE DATOS "BASEDEDATOS.DB"

import _sqlite3

connection = _sqlite3.connect("database.db")

cursor = connection.cursor()

#CREATE THE TABLE PRODCUTOS
cursor.execute("CREATE TABLE PRODUCTOS (Morado INTEGER,  Naranja TEXT, Amarillo INTEGER)")

#INSERTING THE PRODUCTS IN THE TABLE
n=1
while n <= 3:
    contenprod = [(input('ID = '),input('Nombre = '),input('Precio = '))]
    cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", contenprod)
    n += 1

#CONSULT
cursor.execute("SELECT * FROM PRODUCTOS")
personas = cursor.fetchall()

for persona in personas:
    print(persona)


connection.commit()
connection.close()

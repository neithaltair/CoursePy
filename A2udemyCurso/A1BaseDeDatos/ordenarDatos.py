import _sqlite3
# Se genera la conexion con la base de datos
conexion = _sqlite3.connect("basedatos1.db")
# El cursor indicara que ira en la base de datos
cursor = conexion.cursor()
# CURSOR EXECUTE , el comandoa ejecutar en la base de datos
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
# la variable capturara los datos del cursor
ordenedad = cursor.fetchall()

for persona in ordenedad:
    print(persona)

conexion.close()
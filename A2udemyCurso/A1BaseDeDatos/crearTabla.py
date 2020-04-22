import _sqlite3

#Conexion con la base de datos
conexion = _sqlite3.connect("basedatos1.db")
#Se utiliza para ejecutar sentencias en la base de datos
cursor = conexion.cursor()
#Objeto para ejecutar secuencias sql en la base de datos
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
#Se establece que la base de datos guardara los comandos ejecutados
conexion.commit()
#Se debe cerrar la conexion como en los ficheros
conexion.close()
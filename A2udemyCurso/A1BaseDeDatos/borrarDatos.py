import _sqlite3

conexion = _sqlite3.connect("basedatos1.db", timeout=10)

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'NEITH'")

conexion.commit()
conexion.close()
import _sqlite3

conexion = _sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS  VALUES ('NEITH','ALTAIR','MACHUCA',50)")

conexion.commit()

conexion.close()
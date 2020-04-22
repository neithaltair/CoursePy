import _sqlite3

conecction = _sqlite3.connect("basedatos1.db")

cursor = conecction.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 30 WHERE nombre = 'Neithan'")


conecction.commit()
conecction.close()


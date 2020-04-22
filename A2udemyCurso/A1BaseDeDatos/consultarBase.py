import _sqlite3

conexion = _sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

#Fetchall recoge toda la ejecucion del execute
personas = cursor.fetchall()

for persona in personas:
    print(persona)


conexion.close()
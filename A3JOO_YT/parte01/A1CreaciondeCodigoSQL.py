import sqlite3
import pandas as pd

conexion=sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')
cursor = conexion.cursor()

sqlTablaEstudiante = "CREATE TABLE estudiante (carnet TEXT, nombre TEXT, apellido TEXT, carrera TEXT, semestre INT," \
                     "Constraint carnet_pk PRIMARY KEY (carnet))"
#Codigo SQL a ejecutar
cursor.execute(sqlTablaEstudiante)

#Comando que permite ejecutar una tabla de sistema
sqlConsultaTablas = "SELECT * FROM SQLite_master WHERE type=\"table\""

cursor.execute(sqlConsultaTablas)

print("TABLAS DISPONIBLES EN LA BASE DE DATOS:")

#OBTENER EL CONJUNTO DE TABLAS, TODOS LOS RESULTADOS QUE RETORNA LA CONSULTA
tablas = cursor.fetchall()

for t in tablas:
    print('Nombre tipo objeto en la BD:', t[0])
    print('Nombre objeto BD:', t[1])
    print('Nombre tabla:', t[2])
    print('Sentencia SQL:', t[4])

#3
#INSERCION DE DATOS para agregar EN LA BD
datos = [('1001', 'Edward', 'Ortiz', 'Informatica', 5),
        ('1002', 'Daniel', 'Lopez', 'Sistemas', 4),
        ('1003', 'Ramiro', 'Arias', 'Software', 2),
        ('1004', 'Julian', 'Bernal', 'Meca', 8)]

#EL TRY ES POR SI NO HAY INTEGRIDAD DE DATOS
#Codigo de error integrity error, se produce si la llave primaria se repite
try:
    sql = '''INSERT INTO estudiante (carnet, nombre, apellido, carrera, semestre) VALUES (?, ?, ?, ?, ?) '''

    cursor.executemany(sql, datos)
except sqlite3.IntegrityError as e:
    print('Error SQLite:', e.args[0])

#Despues de realizar insercion de datos realizar commit
conexion.commit()

#4
#Ejecutar la sentencia SQL para insertar registros y consultar por un Estudiante
sql = "SELECT * FROM estudiante WHERE carnet='1004'"
cursor.execute(sql)
resultado = cursor.fetchall();
print("\n", resultado)


#5
#Guardar el contenido de la tabla Estudiante en un archivo CSV con Pandas
print()

#Convertir datos de la BD en un archivo CSV
sql = "SELECT * FROM estudiante"
df = pd.read_sql_query(sql, conexion)
df.to_csv('estudiatnes.csv', index=False)


#6
#Finalizacion de la primera demostracion de manipulacion de una BD


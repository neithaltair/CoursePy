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
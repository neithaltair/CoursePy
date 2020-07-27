import sqlite3
import pandas as pd

conexion=sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')
cursor = conexion.cursor()

sqlTablaEstudiante = "CREATE TABLE estudiante (carnet TEXT, nombre TEXT, apellido TEXT, carrera TEXT, semestre INT," \
                     "Constraint carnet_pk PRIMARY KEY (carnet))"


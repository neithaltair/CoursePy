import os

directorioActual = os.getcwd()

metadatos = os.stat(directorioActual)

print(metadatos)
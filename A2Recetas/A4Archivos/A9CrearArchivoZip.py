#Receta 4-9: Crear un archivo Zip

from zipfile import ZipFile

#Para crear un zip con multiples archivos se hace uso de la misma variable
nuevoArchivo = ZipFile('archivo.zip', 'a')
# nuevoArchivo es la variable relacionada al nuevo archivoZip
nuevoArchivo.write('paises.csv')

#Prueba, creando otro zip dentro del mismo codigo
otroZip = ZipFile('archivo2.zip','a')
nuevoArchivo.write('productos.xml')
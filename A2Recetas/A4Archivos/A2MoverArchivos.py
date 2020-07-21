#Receta 4-2: Mover un archivo

import shutil
# ('Archivo a mover', 'nuevo directorio', 'hacer uso de la funcion copiar')
shutil.move('paises2.csv','sub-directorio', copy_function=shutil.copy)

# se debe tener el directorio en la carpeta actual, en este caso en la carpeta archivos
# estamn los codigos y el csv, y el subdirectorio donde se va a colocar el csv


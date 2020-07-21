#Receta 4-1: copiar un archivo

#copy()
#Realiza la copia del archivo en la ruta que se encuentra
import shutil 

#('archivo que se copiara', 'nombre que tendra el archivo copiado')
ruta_nuevo_archivo = shutil.copy('paises.csv','paises2.csv')

#('imprime el nombre que tendra la copia')
print(ruta_nuevo_archivo)

#copy2()
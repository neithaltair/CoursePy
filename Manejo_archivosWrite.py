from io import open 

archivo_texto=open("archivo.txt","a")

archivo_texto.write("\n Esta es la forma de anexar contenido")

archivo_texto.close()
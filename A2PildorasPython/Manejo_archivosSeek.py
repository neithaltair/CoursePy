from io import open

archivo_texto = open("archivo.txt","r")

#SEEK posiciona el puntero para que desde alli empiece a leer
archivo_texto.seek(10)

#READ leera desde el inicio hasta la posicion establecida
print(archivo_texto.read())
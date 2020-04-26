from io import open

archivo_texto = open("archivo.txt","w")

frase = "neithaltair machuca \n bernal"

archivo_texto.write(frase)

archivo_texto.close()
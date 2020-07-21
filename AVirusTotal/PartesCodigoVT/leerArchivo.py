#FUNCION PARA LEER LOS HASH LINEA POR LINEA 
def readFile():
    #Metodo que abre el fichero de los HASH y llama la funcion para realizar la consulta
    with open('hash.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        for l in lines:
            getHash(l)


def getHash(hash):
    print(hash)


readFile()
getHash()
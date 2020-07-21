import json
import time
from virus_total_apis import PublicApi
#NECESARIO TENER EL ARCHIVO otenerHash.txt
# REALIZAR CAMBIO DE LA KEY DE LA API DE VIRUSTOTAL
API_KEY = "5cf60a4ea864eec319e966f64b8c322e2b48fbab98d91fa607f53d35eb7ab2be"
api = PublicApi(API_KEY)
#REALIZA LA CREACION DE EL ARCHIVO A ESCRIBIR
crea = open("hashObtenidos.csv","wt")
#AGREGA LA PRIMERA FILA PARA SEPARAR POR COMAS
tipValue = "Tipo,Value"
crea.write(tipValue); crea.close()

#FUNCION PARA LEER LOS HASH LINEA POR LINEA 
def readFile():
    #Metodo que abre el fichero de los HASH y llama la funcion para realizar la consulta
    with open('hash.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        for l in lines:
            getHash(l)

#FUNCION PARA REALIZAR LA CONSULTA
def getHash(hash):
    response = api.get_file_report(hash)
    with open("response.json", "w") as f:
        json.dump(response, f, indent=4) 
    leeJson(); time.sleep(20) 

#FUNCION PARA ANEXAR LOS HASH AL ARCHIVO TXT
def leeJson():
    with open('response.json') as file:
        data = json.load(file)
    #Asignacion a las variables los valores de los hash
    try:    
        md5 = data["results"]["md5"]
        sha1 = data["results"]["sha1"]
        sha256 = data["results"]["sha256"]

        #ARCHIVO EN EL CUAL SE VA A ANEXAR LA INFORMACION
        archivo = open("hashObtenidos.csv", "at")
        list1 = [md5, sha1, sha256]
        list2 = ["md5", "sha1", "sha256"]
        for v1, v2 in zip(list1, list2):
            cadenaIncluir = "\n"+v2+","+str(v1)
            archivo.write(cadenaIncluir)
        archivo.close()

    except:
        #En caso de ser id unico, se resalta en el documento
        print("id unico")
        valor = data["results"]["resource"]
        archivoId = open("hashObtenidos.csv", "at")
        incluirID = "\n"+"IdUnico,"+valor
        archivoId.write(incluirID)
        archivoId.close()


readFile()
getHash()
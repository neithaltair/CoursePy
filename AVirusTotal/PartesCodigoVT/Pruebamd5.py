import json, pandas
import time
from virus_total_apis import PublicApi
# ...
API_KEY = "5cf60a4ea864eec319e966f64b8c322e2b48fbab98d91fa607f53d35eb7ab2be"
api = PublicApi(API_KEY)


def readFile():
    #Metodo que abre el fichero de las IPs y comienza a llamar otras funciones
    with open('ips.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        for l in lines:
            getIPinfo(l)



#def readFile():
	#Metodo que abre el fichero de los hash y comienza a llamar otras funciones
#	with open('hash.txt', 'r') as f:
#		lines = [line.rstrip() for line in f]
#		for l in lines:
# 			getIPinfo(l)
def leeJson():
    with open('response.json') as file:
        data = json.load(file)
    md5 = data["results"]["md5"]
    sha1 = data["results"]["sha1"]
    sha256 = data["results"]["sha256"]

    fichero = open("anexarTexto.txt", "at")

    list1 = [md5, sha1, sha256]
    list2 = ["md5", "sha1", "sha256"]
    for v1, v2 in zip(list1, list2):
        cadenaIncluir = "\n"+v2+" "+str(v1)
        fichero.write(cadenaIncluir)

    fichero.close()




array = [
"4a88e83b325aa23da1e4bfa90b4f7c34",
"7c511342c81d95b8ea92eb279ad7685f",
"84557e5a34eca7881ea9533e1cf44d68",
"def9984e70a640928851304ab4c2ee97",
"bb230c7e3206106dafa7b90a5f615181",
"036de94464c86c3fdc973e4c601d7dbf",
"738ff32e2cf3378cac040f21727a6322",
"341c49168e101ac33cb45f62e13054c2",
"1167654ff0c444d3ee7e520391a3a291",
"e670a4999900ccbca5de1765556c0731",
"b586c2def1c49c00187a53da1a2215e7",
"ca9480c80d22f8f30f65ea5299e8bed1",
"987413c576a09aa5798bc1bebe099dfd",
"2fa666498f3ec42f9c276b1033d48e55",
"ec080c8f537441893c201ca4a9707ab3"
]

print(len(array))


#FUNCION PARA LEER LOS HASH LINEA POR LINEA 
def readFile():
    #Metodo que abre el fichero de las IPs y comienza a llamar otras funciones
    with open('hash.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        for l in lines:
            getHash(l)



#FUNCION QUE RECIBE EL VALOR DEL HASH 
def getIPinfo(ip):
    #Metodo que consulta en IPinfo una direccion IP para obtener informacion de la misma
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)
    dic = {}
    dic = details.all
    jsonlist.append(dic)


def getHash(hash):
    print(hash)
    #
    #response = api.get_file_report(hash)
    #with open("response.json", "w") as f:
    #    json.dump(response, f, indent=4)
    #print(x) 
    #leeJson()
    #time.sleep(20)        
    #___________________________________
    #handler = ipinfo.getHandler(access_token)
    #details = handler.getDetails(ip)
    #dic = {}
    #dic = details.all
    #jsonlist.append(dic)


#PARTE DEL CODIGO QUE RECORRE EL ARRAY PARA IDENTIFICAR LOS HASH
for x in range(0,len(array)):
    hash = array[x]
    print(hash)
    response = api.get_file_report(hash)

    
    with open("response.json", "w") as f:
        json.dump(response, f, indent=4)
    print(x) 
    leeJson()
    time.sleep(20)        
       
    
    


            

    
    
#4 solicitudes por minuto 
#Solo se pueden realizar 4 solicitudes por minuto
#terminar de cuadrar los hash para que realice la respectiva consulta
#quiza sea necesario cambiar el while 
#mirar otras formas de recorrer los arreglos para poder tener el resultado 
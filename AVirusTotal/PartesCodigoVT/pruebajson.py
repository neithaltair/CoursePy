# Extraer info del json

import json




def leeJson():
    with open('0response.json') as file:
        data = json.load(file)
    md5 = data["results"]["md5"]
    sha1 = data["results"]["sha1"]
    sha256 = data["results"]["sha256"]

    fichero = open("anexarTexto.txt", "at")

    list1 = [md5, sha1, sha256]
    list2 = ["md5", "sha1", "sha256"]
    for v1, v2 in zip(list1, list2):
        cadenaIncluir = "\n"+"Tipo "+v2+" Hashes "+str(v1)
        fichero.write(cadenaIncluir)

    fichero.close()


if __name__ == "__main__":
    leeJson()

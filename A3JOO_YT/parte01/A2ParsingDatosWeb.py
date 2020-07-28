import requests
import feedparser
#Se realiza la instalacion de feedparser

#Realizar solicitud sencilla a una pagina
url = 'https://github.com/neithaltair/CoursePy'
respuesta = requests.get(url)
print(respuesta)

#Obtener todoo el codigo html de la pagina web
print()

html = respuesta.text
print(html)
print()

#OBTENER LA RESPUESTA EN JSON
print(respuesta.json)

#INFORMACION DE LOS HEADERS, ENCABEZADO DE RESPUESTA GENERADA POR SERVIDOR
print()
headers = respuesta.headers
print(type(headers))
print(headers)

print()
#CONSULTAR CODIFICACION
print(respuesta.encoding)
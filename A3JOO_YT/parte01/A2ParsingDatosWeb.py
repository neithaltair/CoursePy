import requests
import feedparser
#Se realiza la instalacion de feedparser

#Realizar solicitud sencilla a una pagina
url = 'https://github.com/neithaltair/CoursePy'
respuesta = requests.get(url)
print(respuesta)
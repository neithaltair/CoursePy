#Sub
import re

#Cambia el contenido de la variable por otra
texto = "la silla es negra y para jugar"

#Remplaza "para jugar" con "de gamer"
print(re.sub("para jugar","de gamer", texto))
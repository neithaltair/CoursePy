#HTML CON PYTHON

import pandas as pd

url = 'https://en.wikipedia.org/wiki/Cristiano_Ronaldo'

dataFrame = pd.io.html.read_html(url)

print(dataFrame)

dataframeFinal = dataFrame[0]

print(dataframeFinal)

#Pasar el contenido a diccionario
print(dict(dataframeFinal.loc[0]))


#REVISASR VIDEO DE UDEMY, VIDEO 123

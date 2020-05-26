#HTML CON PYTHON

import pandas as pd

url = 'https://www.virustotal.com/gui/file/f4bbbf23177f13d499cfc59eb5cbd3bbb7ac2e0bbe899ab3f1315963bf58725d/details'

dataFrame = pd.io.html.read_html(url)

print(dataFrame)

dataframeFinal = dataFrame[0]

print(dataframeFinal)

#Pasar el contenido a diccionario
print(dict(dataframeFinal.loc[0]))


#REVISASR VIDEO DE UDEMY, VIDEO 123

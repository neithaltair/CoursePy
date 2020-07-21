#Receta 4-4: leer el contenido de un archivo XML

import xml.etree.ElementTree as ET 

archivoXml= ET.parse('productos.xml')

#Obtener el elemento padre (raiz)
raiz = archivoXml.getroot()
print(raiz)

#Obtener los elementos hijo con for 
for hijo in raiz:
	print(hijo)

#Imprimir el texto de cada elemento
for hijo in raiz:
	print(hijo.text)

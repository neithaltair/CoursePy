#findall
import re


texto = """
El carro de luis es amarillo
Mi carro es negro
El otro carro es rojo
"""

#Realiza la busqueda de las palabras dentro del texto
print(re.findall("carro.*amarillo", texto))

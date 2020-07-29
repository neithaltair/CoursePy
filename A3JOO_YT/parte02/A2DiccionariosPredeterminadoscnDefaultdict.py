#34
#DICCIONARIOS PREDETERMINADOS CON DEFAULTDICT
from collections import defaultdict

versionesLeng = defaultdict(lambda: '1.0.0')
versionesLeng ['Java'] = '12.0.0'
versionesLeng ['Python'] = '7.1.0'
versionesLeng ['PHP'] = '4.3.6'

print(len(versionesLeng))
print(versionesLeng)
print(versionesLeng['Java'])
print(versionesLeng['PHP'])
print(versionesLeng['Python'])
print(versionesLeng['C# '])

#35 = CONTEO DE OCURRENCIAS DE CADENA DE CARACTERES CON UN OBJETO DEFAULTDICT
print()

lenguajes = 'Python JS PHP C# Java C++ C PHP Python JS JS Java'
#SE hace uso de split para separar las palabras por espacio
lenguajes = lenguajes.split()
print(lenguajes)

conteo_lenguajes = defaultdict(int)
for l in lenguajes:
    conteo_lenguajes[l] += 1

print(conteo_lenguajes)
print(conteo_lenguajes['Python'])
print(conteo_lenguajes['C'])
print(conteo_lenguajes['Kotlin'])
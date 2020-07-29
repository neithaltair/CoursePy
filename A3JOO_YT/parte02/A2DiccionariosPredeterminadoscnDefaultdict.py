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



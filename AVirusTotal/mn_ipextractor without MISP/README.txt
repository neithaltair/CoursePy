======================================================================
Author: Jose Luis Sanchez Martinez
Author: Jose Moya Villalba
Language: python 3
======================================================================
DESCRIPCION:
Script que tiene como objetivo sacar informacion de direcciones IP de dos fuentes principalmente, exportando los resultados a JSON y Excel.
1. IPinfo.io: Obtencion de informacion sobre las direcciones IP, como ASN, Paises, Ciudades, etc...
2. aSight: Obtencion de los eventos donde se encuentran las direcciones IP (En caso de que sean IOCs)

NECESIDADES:
Antes de la ejecucion, se necesita instalar el fichero requirements.txt con pip3.
Es necesario que exista un fichero llamado ips.txt que contenga linea por linea la direccion ip que se desea analizar.

USO:
El uso es muy simple: python3 mn_ipextract.py

El resultado sera un fichero JSON y otro fichero Excel.

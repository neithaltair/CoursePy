import ipinfo, json, pandas, requests
from pandas.io.json import json_normalize

def readFile():
	#Metodo que abre el fichero de las IPs y comienza a llamar otras funciones
	with open('ips.txt', 'r') as f:
		lines = [line.rstrip() for line in f]
		for l in lines:
			getIPinfo(l)
			

def getIPinfo(ip):
	#Metodo que consulta en IPinfo una direccion IP para obtener informacion de la misma
	handler = ipinfo.getHandler(access_token)
	details = handler.getDetails(ip)
	dic = {}
	dic = details.all
	jsonlist.append(dic)

def generateJsonFile():
	#Metodo que genera una lista de diccionarios con las informaciones que obtiene de IPinfo
	with open('_output_json_ips.json', 'w') as outputfile:
		json.dump(jsonlist, outputfile)
	json_toXlsx()

def json_toXlsx():
	#Metodo que genera el fichero excel en base al JSON
	output_excel = "_output_excel_ips.xlsx"
	try:
		with open('_output_json_ips.json') as file:
 			data = json.load(file)
 			normalizedJson = json_normalize(data)
 			normalizedJson.to_excel(output_excel,verbose=True,sheet_name='datos',encoding='utf-8')
	except FileNotFoundError as identifier:
		print("El fichero JSON no se ha encontrado")


if __name__ == "__main__":
	access_token = '9454b1263b326e'
	jsonlist = []
	readFile()
	generateJsonFile()

import json, pandas
import time
from virus_total_apis import PublicApi
# ...
API_KEY = "5cf60a4ea864eec319e966f64b8c322e2b48fbab98d91fa607f53d35eb7ab2be"
api = PublicApi(API_KEY)

#FUNCION PARA LEER LOS HASH LINEA POR LINEA 
def readFile():
    #Metodo que abre el fichero de los HASH y llama la funcion para realizar la consulta
    with open('hash.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        for l in lines:
            getHash(l)

#FUNCION PARA REALIZAR LA CONSULTA
def getHash(hash):
    print(hash)
    response = api.get_file_report(hash)
    with open("response.json", "w") as f:
        json.dump(response, f, indent=4)
    print(x) 
    leeJson()
    time.sleep(20) 

#FUNCION PARA ANEXAR LOS HASH AL ARCHIVO TXT
def leeJson():
    with open('response.json') as file:
        data = json.load(file)
    md5 = data["results"]["md5"]
    sha1 = data["results"]["sha1"]
    sha256 = data["results"]["sha256"]

    fichero = open("anexarTexto.txt", "at")

    list1 = [md5, sha1, sha256]
    list2 = ["md5", "sha1", "sha256"]
    for v1, v2 in zip(list1, list2):
        cadenaIncluir = "\n"+v2+","+str(v1)
        fichero.write(cadenaIncluir)
    fichero.close()

readFile()
getHash()
leeJson()


array = [
"0220989abbb3a21722f57117c7fe36107336e5156978040b4398095f4ae107ea",
"ba244c534e6a0eedb496e840881c5401c3640fc317b601da17ca84570e1e181a",
"8848b8bcd2601b3133730d50d09fab800625efb88e98897b9f4f116109d3406c",
"18fd12b1373834481ce1361997fb65065b52891f493b10bfdeb721ef7cb88c8e",
"d9a42415425f83463e33009c502f02931320a9bc602c18ecc3b4526cc99e9a6a",
"764de329971bfad39b34170b9c58cce870c45139cc813db3f6eb5f34be3fa565",
"0d204a3dcd80cbbf3063bfa130f163a4281c56bab9a5017faf6307025b5c829d",
"ad784acea8679e3e4c93da4947b9419d968f990fdd8720bbf40aaef6e10bab91",
"6cc095d21659b30833d3d8aa84025b7b27783f13f220e32b3c13384deb46ea96",
"1c76b631dd54f736e8bf3c822ab85e167c91fa18f19b7f38cc57e0aa4cfb6511",
"fe3101741d7d2dc5cad629417ff785ff65b2f7ce08686719eb3d730e4fb1d83e",
"967077efd6c03facd18f7ba17ca3aa059546b645cc2dae9e063a74848d9158c8",
"42748e1504f668977c0a0b6ac285b9f2935334c0400d0a1df91673c8e3761312",
"89e14c2a5cff2df052f04dfd18aab04e6d27050c8122db7501d3bf71c5443f67",
"cef2b5760d8f9a6a1afc78e376fc317e95b179791bc789331849c7c70d007966",
"243523bc473510cb599d2178cad163fc964d8d5a888c7fbf902234586d90ef1a",
"6d54ae0794a3210ba8e4f7d484a95f65023406ab354ca506c1deeb63aecb2d00",
"e1fcaae28ea45d7c16358403343907cd8c2be8db76247e434645cfb200686e01",
"3397e99f1106de38020f455389ddc1a5f9e35d8e61ec9c43080ee53594849feb",
"22995df40a3f88235680c1026c2888f64eeedaf7099a38288e683a61ac111145",
"0b4cd81fb8dca48e80539d27eb91080f9aa2ce7cd6c746c9c0e47c1a337bf571",
"f6772a0bc1c0d5bf9d5351feb655521680589e38481f7e67e111ea4d329e7dd5",
"8f5549e8c7fecbd891753f52477eaa8a0e165d4c5838f2f420a75dce946d44c6",
"70450e7986dc7f6f5a321ba79f666b0eb1e5becf026add09e90e38ece9b764b2",
"636a3afd83b95c3b4b55ff23bee01484a177d4840eb1f1e93c84852b9b5ff854",
"3a31999bff1c0e6b4a0086942e67f698a46ad8f9cdbe6010ddde8c421c167b0f",
"478c5c963572b90f663399aac930d55f1ae4d8c69d3a0c83a70db6ee9e9c4202",
"da6a7c687dfd9d4a84ca77dcaa48fbc8de0e1613ea7691ef0bc361f4b4eabe7e",
"045db284e68d38f8af6c6e805197ca3b384bb682ead3d4c15b8428790482a2b4",
"b1610f813b6ba3d4b50f4f6036e6d6582c7834f3b0d28d09734139c92d7bd1a4",
"e75465cd7994155eba57106d92a02fb6439ec1f44451db112b970d749e3f4e3b",
"513a9d7924d72162704c8d6eab1172aac239a5f96dfebd121a2f9710d9f382ad",
"2ba0f2e22ed07ca3188c898a0c9256fd30e878916ebe669ed52b25cb18d5ccde",
"3cb0e9b7c28f2456452744f8c5ca77775b581c96bb30284a97e0f89a035f3781",
"d7d6564e6ec76c7172bf6d9fcef41b7d471d03682a176287c2ad78751c593df1",
"740592a2882555a2ec8ae24aac692ce39d77ea7fb1616cce624a8cad46cd4469",
"e04b3a9850cf32ceb122a7b1bec0d9981bba84ca8835867408dcafbca18fcb40",
"57a02c7e2f04a1e8adeca40d9d3b5b152f6cc20fe1b817dca1e573cdb2407723",
"a641b18b04a5b11525152f9ece163ba54c5d57713b859e9a097000aa58eb896f",
"b1532a52821c2402f9d889c07663246bed7b3a1e257999e18cdde29b7a685353"
]

print(len(array))

for x in range(0,len(array)):
    hash = array[x]
    print(hash)
    response = api.get_file_report(hash)

    
    with open("response.json", "w") as f:
        json.dump(response, f, indent=4)
    print(x) 
    leeJson()
    time.sleep(20)        
       
    
    


            

    
    
#4 solicitudes por minuto 
#Solo se pueden realizar 4 solicitudes por minuto
#terminar de cuadrar los hash para que realice la respectiva consulta
#quiza sea necesario cambiar el while 
#mirar otras formas de recorrer los arreglos para poder tener el resultado 

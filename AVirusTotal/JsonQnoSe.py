import json, pandas
import time
from virus_total_apis import PublicApi
# ...
API_KEY = "5cf60a4ea864eec319e966f64b8c322e2b48fbab98d91fa607f53d35eb7ab2be"
api = PublicApi(API_KEY)



#def readFile():
	#Metodo que abre el fichero de los hash y comienza a llamar otras funciones
#	with open('hash.txt', 'r') as f:
#		lines = [line.rstrip() for line in f]
#		for l in lines:
# 			getIPinfo(l)
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
        cadenaIncluir = "\n"+v2+" "+str(v1)
        fichero.write(cadenaIncluir)

    fichero.close()




array = [
"ea97e8b77b654598a46a12f6f80ace614cd0cc0b6e2060e81ca2c76ec1f9e2e8",
"201f31c84755a5cd6081c3db30626cc3f17cf84804c2deb66e27866daad259a3",
"cb06287e314bf4c684323c7925922cce2932a9e9e9b6aac34634487ac7741afd",
"e91586b66e6d05e3b118991b72896d37c3e625e4f54ceb4ad6b04f047a31593b",
"3295199ba2b4e9cfc448a574cb9e89f3ef131fd19dcf366fe2abb7b3b79eb887",
"81a857d256dbd90322fa437e8045e2e2173fce46ef05cf83df9b8fe8f62bf74c",
"39d798c7b1fa8a57dba656682d2c91beb946e10c277ad12e2b08a7b7c1d88a8c",
"8284d1613e68ccfd1f07b80161e38f9a96cf26f1229cd297ea1bd95809459bdd",
"32eda28241805e739ecdf205f056948cd4bc0d421ccfb70e77d1027d94504587",
"b1d5be14b2011f0628dcdd686183f2a2363febdac7e14f23eb51ffd7238b9ba2",
"572a2d0e60147163deb9bbada3ddd7fe414096fc1b14f51bd6d17a0fc34e7131",
"447ccb93bcbc969e08ec726e1461c386668720d79d091bca889b5b5a129a352d",
"4a30c6c89f0d95bc647da438bb4783853167f997221b3ff91bda6816d4043c5a",
"52e66bc19323536314fce12a2a3fa064b726bb71704a0d9f899d49892f265274",
"b55075d58564ce37324e5f4c746839e35293ac60fed35f345163b77944b0ed8d",
"3ec311c131d15a530dac35108f167ee926ef87e6cef618c6ba05d9eb239a4940",
"f3b00f34857586056178a56517e4c07effe1182604b11665fb8efb71be78cec4",
"5cce814cadb4fac6631ff3c988516b4c6618f0c71c7de3588fc0d7038c220f31",
"99e316f57528b47af726ff2cd9a33f6c950c4c7f6b88174d491510eb44047132",
"44de5a248b6e9c24ad547e73c3ba3c8cc9693ba6eaa5190be9b377845844ffb6",
"0a3bdfe88cf7c38294a1ff2a497f3bcedb3feb8dc37fa0de7332865c348b7eb0",
"434733d083f2648719bc02e7c8b0bf300007619f20876cb9161e88f5a13d47f2",
"1868425310156eafad6074aab9b3bff4c681615a03914f7b970d9e7bc476bbb0",
"230f27eb5652c0a169740a44375221bcda1fae8c3703e354bb756189fa0b8a07",
"bf1c8cf3ab6213c250d1abf8094180fdcf8e871674482fce1930abe9826e61b9",
"478cf5482905fa2ac2a2280a03ad6716f153c372c15cd957a23a67ff3260c867",
"b0faa36c459996787f5aadb327003497444c375e25d0e6a07bc7264608f6b18a",
"40d48f5e965a250ac45f2f9c9426743c66fe899f07e16c42339149e30b1956e9",
"a1396856c94b92cc78e9636b37ed3e998443699d6bb9f35e086bc87a5ccd0f67",
"0fa8acdb672f0e6c184fc5d04bb8af92c0bf5db73de096606f23f4c38ef3347b",
"17ab5394041bf8230f816ea92638ec5e5515112132a8e649d4caa783d886cfdf",
"eb12c86b21b337b64f99ad7f7375bc4bbb05a7ba6b5af605ace55546af9db222",
"0de5f042eb250092454d786b6303dee434202d45dc3fec9e6b39237f9e92514f",
"83358d06da03686a452f03045219f8286d46ada3287b3a354229ae82dcbd3266",
"808680e6761782a7817fd8e3f90463738d17216b3bca51f3ca4e7375458cba1b",
"d9f5fe4cd4885a31c288e89447db5d77e846db5b714bb6c1a32e8692e9dd6acd",
"9f2bb6a03ce289a2b6b10950df6ccf80ef3f25dfc2a8c0c9fa5efb3b76e1c167",
"b75354d8ad3f4e0f675ec6a64c82226d75116535198ef4974b17984ccebab63e",
"5174ef9f7d5420ab4890173792d8aafc50b8bb3191b4c24f6f58ae73bd7212c3",
"47070e4f6545f9f1308a5aec1e6943e6a29891bce9523db5596544a52f9b3bf4",
"f36626f1a71c68c4647347b25eb0000c0e6c5d7700cf16047a3d9967321cf14b",
"eafa30bac261cc682556812c7c513827f09ef75fc33dbeb61e5d3ff46c9f3808",
"ba59847f9f160987ee5d9ad57d5022895cece9bd4627d90f5eab35c2f29596ea",
"ed6338943d6237d422e4c54ad3e33040140de6800717831c071de1a37fdf1fe9",
"23a2e7637acc101bf40ddc953152d7302342e3ca480353a84f6fee5e23155519",
"24c3d64db7c499c6c60ae6bf406e25d6a70902cb7f2393b81555e3241aa7c43c",
"ee1b2b016b56950986db7b08f451220b91f1d91a70fec0624e289e96c648cb44",
"1a230bb362cde9ead2d9f867af181ae51292c626a3c9d1d30f5f3751b84ffe85",
"7c7264939bd4e249e559f507027c1b1eb92541803e29434238165423c664fa8a",
"a3bd7d3e7006439d1d53cf8db1f403df2162c8f7e8172d6911be203ea58a2d8d",
"054f55d77f0250760ab3a12e63af89ba5958468215e18b522cd618363da938a1",
"10667e9d67706397f7ff96e892d3c0f0ae05d81df5bc17caf85fb356d531c0b8",
"7c43ad507d71361001464838d5a55a4753a4c8c0e9647de37e721a2d86fb5a86",
"531ed45fca9530ae8d1b56b40b784c8d238bf739ea1c7d5779a7dc155248f47b",
"5a882cb5120fc2720df4c26a02feafcac4246c7937c7dcb6046a1f185e39a2eb",
"7f97ba9a8e6b70708a001cff8677992fc1e768a62f9f21ddd14fb1c6924281bc",
"9ad437d76f08dcb1ce86da07de067735d5b9c657c91ffb13972addce1d50cade",
"96b4836f4e0e5293833e30db86660e5e45268f4a2072fbbeea8003b684756d45",
"7e1aa75831ab42fb27bd372c84e70816cee68e63c59ab66ad445e123cb4dad40"
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

#Agregar nueva informacion al fichero
#A= hacer referencia al append, que es agregar informacion
#T= Hace referencia a que sera contendio texto(caracteres)
#CREAR EL archivo
#REALIZA LA CREACION DE EL ARCHIVO A ESCRIBIR
crea = open("hashObtenidos.csv","wt")
tipValue = "Tipo,Value"
crea.write(tipValue)
crea.close()

escribeArchivo = open("hashObtenidos.csv","at")

#Haciendo uso de el salto de linea y concatenando el input
#Se logra que el contenido nuevo haga parte de un nuevo renglon
#en el texto



#colocar en un arreglo los valores de los hash y recorrerlos tambien
emede = 555555
eseachea = 111111111
doscincuenta = 256256256256

list1 = [emede,eseachea,doscincuenta]
list2 = ["md5","sha1","sha256"]


for v1, v2 in zip(list1,list2):
	cadenaIncluir ="\n"+v2+","+str(v1)
	escribeArchivo.write(cadenaIncluir)

escribeArchivo.close()
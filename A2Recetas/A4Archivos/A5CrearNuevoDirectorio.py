#Receta 4-5: crear carpeta 

import os 

nuevoDirectorio = 'NuevaCarpeta'

if not os.path.exists(nuevoDirectorio):
	os.makedirs(nuevoDirectorio)

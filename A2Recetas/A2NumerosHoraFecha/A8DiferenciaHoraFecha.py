#Diferencia entre horas y fechas

import datetime
import time

#Se busca establecer la diferencia entre una fecha y la otra
fecha1 = datetime.datetime.now()
#Se establece un delay para que sea evidente la diferencia, espera seis segundos para
#ejecutar la siguiente linea de codigo
time.sleep(6)
fecha2 = datetime.datetime.now()

#se calcula la diferencia
diferencia = fecha2 - fecha1

print(diferencia.seconds)


delta = datetime.timedelta(days=7)

fechaResultado = fecha2
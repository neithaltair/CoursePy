#Fecha y hora

from datetime import datetime

fechayHora = datetime.now()

print(fechayHora)

# sacar  fecha parte por parte
anio = str(fechayHora.year)
mes = str(fechayHora.month)
dia = str(fechayHora.day)

print(anio+"\n"+mes+"\n"+dia)


#Hora

hora = fechayHora.hour
minutos = fechayHora.minute
segundos = fechayHora.second
microseg = fechayHora.microsecond

print("La hora es {}: {}: {}...{}".format(hora, minutos, segundos, microseg))
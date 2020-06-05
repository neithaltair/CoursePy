import datetime

horaFechaActual = datetime.datetime.now()

print(horaFechaActual)

hora = horaFechaActual.time()
fecha = horaFechaActual.date()

print('\nHora y fecha actuales',hora)
print(fecha)
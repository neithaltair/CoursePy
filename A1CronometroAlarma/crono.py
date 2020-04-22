from datetime import datetime
from time import sleep
from tkinter import messagebox
import tkinter


#DATE TIME
fechayHora = datetime.now()

def alarma():
    #Se obtiene la hora actual
    hora = int(fechayHora.hour)
    minute = int(fechayHora.minute)
    second = int(fechayHora.second)


    #Se imprime la hora actual
    print("HORA INICIO = ",hora,":",minute,"::",second)


    #Se solicita la hora de recordatorio
    horaAlarm =  int(input("Ingresar Hora = "))
    minuteAlarm = int(input("Minutos = "))
    secAlarm = int(input("Segundos = "))


    print("Alarma activa para esta hora = ",horaAlarm,":",minuteAlarm,"::",secAlarm)
#_________________________________________________
    #VARIABLES
    horaprecisa = 0


    #FUNCION OBTIENE LA HORA
    while(horaprecisa == 0 ):
        fechayHoraActual = datetime.now()
        horaActual = int(fechayHoraActual.hour)
        minuteActual = int(fechayHoraActual.minute)
        segActual = int(fechayHoraActual.second)
        print("\nLA HORA ACTUAL ES = {} : {} :: {}".format(horaActual,minuteActual,segActual))
        print("hora actual = {} minutoactual = {} segundoactual = {}".format(horaActual, minuteActual, segActual))
        print("hora ALARMA = {} minutoALARMA = {} segundoALARMA = {}".format(horaAlarm, minuteAlarm, secAlarm))
        if ((horaActual == horaAlarm) or (horaActual > horaAlarm)) and ((minuteActual == minuteAlarm)or(minuteActual>minuteAlarm)):
            print("TODO IGUAL")
            horaprecisa = 1
            #POPUPS
            raiz1 = tkinter.Tk()
            raiz1.title("POPUPS")
            tkinter.messagebox.showinfo("ALARMA FINALIZADA","ALARMAS FINALIZADAS")
        else:
            print("NO ES IGUAL")
        sleep(1200)





#TKINTER

raiz = tkinter.Tk()

raiz.title("CronoAlarma")

boton = tkinter.Button(raiz, text="Iniciar", command = alarma)
boton.pack()


raiz.mainloop()











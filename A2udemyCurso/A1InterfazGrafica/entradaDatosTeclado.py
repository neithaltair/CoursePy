import tkinter

raiz = tkinter.Tk()

raiz.title("IngresoDatosxTeclado")

#Creamos el componente entry
entrada = tkinter.Entry(raiz)
contenido = input(entrada.config(justify="center"))


entrada.pack()

raiz.mainloop()




if(num == 0):
            print("hora actual = {} minutoactual = {} segundoactual = {}".format(horaActual,minuteActual,segActual))

            print("hora ALARMA = {} minutoALARMA = {} segundoALARMA = {}".format(horaAlarm,minuteAlarm,secAlarm))
            #if((horaActual == horaAlarm) and (minuteActual >= minuteAlarm) and ((segActual == secAlarm) or (secAlarm > secAlarm))):
                #num = 1
            #horaprecisa = num
            if(horaActual == horaAlarm):
                print("HORA IGUAL")
            if(minuteActual == minuteAlarm):
                print("MINUTO IGUAL")
            if(segActual == secAlarm):
                print("SEGUNDO IGUAL")
            else:
                print("NO ES IGUAL")
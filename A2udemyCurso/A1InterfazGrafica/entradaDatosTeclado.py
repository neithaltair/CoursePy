import tkinter

raiz = tkinter.Tk()

raiz.title("IngresoDatosxTeclado")

#Creamos el componente entry
entrada = tkinter.Entry(raiz)
entrada.config(justify="center")

entrada.pack()

raiz.mainloop()
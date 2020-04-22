import tkinter

#es necesario importar el messagebox de forma directa
from tkinter import messagebox

raiz = tkinter.Tk()

raiz.title("POPUPS")


#funcion a ejecutar

def avisar():
    tkinter.messagebox.showinfo("TituloVentana", "Mensaje con la informacion")


#componente
boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()




raiz.mainloop()
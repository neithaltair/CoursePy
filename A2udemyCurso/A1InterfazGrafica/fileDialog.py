import tkinter
from tkinter import filedialog
rais = tkinter.Tk()
rais.title("FileDialog")


#funcion
def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)


#Metodo para fichero
boton = tkinter.Button(rais, text="pulsar para empezar", command = abrirfichero)
boton.pack()

rais.mainloop()
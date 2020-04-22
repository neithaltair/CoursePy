import tkinter

raiz = tkinter.Tk()

raiz.title("UsoBoton")

#creacion del componente boton para ejecutar acccion al pulsar

def accion():
    print("HOLA A TODAS LAS PEEEEEEEERRRAS")


boton = tkinter.Button(raiz, text ="Muestra de contenido", command=accion)
boton.config(fg="green", bg="blue")
boton.pack()

raiz.mainloop()
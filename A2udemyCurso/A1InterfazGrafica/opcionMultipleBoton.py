import tkinter
raiz = tkinter.Tk()

raiz.title("BotonOpcionMultiple")

#funcio

def seleccionar():
    print("la opcion seleccionada es {}".format(opcion.get()))

#variable opcion
opcion = tkinter.IntVar()

#radio buton
radioboton = tkinter.Radiobutton(raiz, text="Opcion 1", variable=opcion, value=1, command=seleccionar)
radioboton.pack()

radioboton1 = tkinter.Radiobutton(raiz, text="Opcion 2", variable=opcion, value=2, command=seleccionar)
radioboton1.pack()

radioboton2 = tkinter.Radiobutton(raiz, text="Opcion 3", variable=opcion, value=3, command=seleccionar)
radioboton2.pack()





raiz.mainloop()
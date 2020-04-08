import tkinter

raiz = tkinter.Tk()

raiz.title("Programa")

#componente frame
frame = tkinter.Frame(raiz)
frame.config(bg="blue",width="600",height="600")
#frame.pack()

#componente programa
texto = "creacion del programa"
etiqueta = tkinter.Label(raiz, text = texto)
etiqueta.config(fg = "black", bg="white", font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()


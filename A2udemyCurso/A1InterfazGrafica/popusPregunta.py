import tkinter
from tkinter import messagebox


raiz = tkinter.Tk()
raiz.title("PreguntaMessageBox")

def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "Ese hijo de su madre?")
    if(resultado=="yes"):
        print("YES HJDSPM")
    else:
        print("No tan HDSPTM")


boton = tkinter.Button(raiz,text="PREGUNTA", command=preguntar)
boton.pack()

raiz.mainloop()
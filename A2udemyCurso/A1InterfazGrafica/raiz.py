import tkinter

raiz = tkinter.Tk()

raiz.title("MI PROGRAMA")

#creamos el componente frame

frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=500,height=500)
frame.pack()



raiz.mainloop()
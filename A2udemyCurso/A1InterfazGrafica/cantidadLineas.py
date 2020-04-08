import tkinter

raiz = tkinter.Tk()
raiz.title("VariasLineasTextoTEXT")

#Creamos nuestro componente text (texto largo de varias lineas)

entrada = tkinter.Text(raiz)
#tambien se pueden agregar margenes con padx y pady, colores tambien
#selectbackground, el color del texto solucionado
entrada.config(width=100, height = 100, font=("Verdana",20))
entrada.pack()


raiz.mainloop()
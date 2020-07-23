#Python 7-1: Obtener el tipo de dato de una variable o de una literal

#1. type()
#2. isinstance()

#SABER QUE TIPO ES LA VARIABLE
a = 5
b = "cadena de caracteres"
print(type(a)); print(type(b))

#Se hace uso del isinstance() para preguntar si son str o enteras
print(isinstance(a,str))
print(isinstance(b,int))
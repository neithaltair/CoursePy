print("Programa de ecaluacion de notas de alumnos")

#Todo input en python es tomado como string, para solucionar esto se debe usar un metodo que 
#convierta el string en int
nota_alumno = input("intorducir la nota del alumno")

 

def evaluacion (nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


#print(evaluacion(nota_alumno))

print(evaluacion(int(nota_alumno)))
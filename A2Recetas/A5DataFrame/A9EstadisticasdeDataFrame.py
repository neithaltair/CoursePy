#Recetas 5-9: Obtener estadisticas de un dataFrame

import pandas as pd

peliculas = pd.read_csv("movies.csv")

print(peliculas.describe())

#Se hace uso del mean para obtener el promedio de la columna
#SE puede hacer uso del max (maximo) y el min (minimo)
print("Imprime el promedio de la columna de facebook_Likes =",peliculas.movie_facebook_likes.mean())

print("Imprime el MAX = ", peliculas.movie_facebook_likes.max())



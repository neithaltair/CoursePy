import pandas as pd
import tkinter
import webbrowser

#apertura de la pagina web
website = 'https://es.wikipedia.org/wiki/Cristiano_Ronaldo'
webbrowser.open(website)

#Mostrara la tabla
dataFrameCR = pd.read_clipboard()


print(dataFrameCR)
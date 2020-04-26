import pandas as pd
import webbrowser

#apertura de la pagina web
#website = 'https://www.netflix.com/watch/81082125?trackId=14170286&tctx=2%2C6%2C8a830c94-f54d-4292-bc54-d771722c735f-38275228%2C249dd359-658b-4300-a7f6-deaa625741ea_110443X3XX1587687750888%2C249dd359-658b-4300-a7f6-deaa625741ea_ROOT'
#webbrowser.open(website)

#Mostrara la tabla
dataFrameCR = pd.read_clipboard()


#Data Frame notas
lista_asignatura = ['matematicas','historia','fisica']
lista_notas = [8,7,9]
diccionario = {'Asignatura':lista_asignatura,'Notas':lista_notas}

print("\nImprime el diccionario = ",diccionario)

#Crear un data frame del diccionario
dataFrameNotas = pd.DataFrame(diccionario)
print('\nCreacion del dataFrame a partir del diccionario\n',dataFrameNotas)
import pickle

frutas = {"apple":"Steve","Microsoft":"Bill", "Amazon":"Besos", "Facebook":"Marck"}

txt = open("diccionario.pckl","wb")
pickle.dump(frutas, txt)

txt.close()



diccionario = open("diccionario.pckl","rb")
dic_leido = pickle.load(diccionario)

print(dic_leido)
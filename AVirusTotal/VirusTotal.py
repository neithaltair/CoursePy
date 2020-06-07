import webbrowser as wb 

while i != 0:
    hash = input("HASH")
    wb.open_new("https://www.virustotal.com/gui/file/"+hash+"/detection")
    i = input("Continuar")

    
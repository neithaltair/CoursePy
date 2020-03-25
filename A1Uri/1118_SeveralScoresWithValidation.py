def valores():
    a = float(input("Valor 1 ="))
    b = float(input("Valor 2 ="))

    if (a>0.0 and a<=10.0) and (b>0.0 and b<=10.0):
        media=(a+b)/2
        print("Media = %.2f" %media)


        c = int(input("Nuevo Calculo 1-si 2-no = "))
        if c==1:
            valores()
                
    else:
        print("Valor nulo") 
        valores()

valores()
CantidadTest = int(input("t =")); i=0;



def population_Incrase():
    anios = 0

    c1 = int(input("Poblacion Ciudad 1 ="))
    c2 = int(input("Poblacion Ciudad 2 ="))

    if (c1 >= 100 and c1 <= 1000000) and (c2 >= 100 and c2 <= 1000000) :
        p1 = float(input("Crecimiento pueblo 1 ="))
        p2 = float(input("Crecimiento pueblo 2 ="))

        while(c1 <= c2):
            crec1 = (c1 * p1)/100
            c1 += crec1
            #print(crec1)

            crec2 = (c2 * p2)/100
            c2 += crec2

            anios+=1
        print(anios,"anios")

        while (c2 <= c1):
            crec1 = (c1 * p1) / 100
            c1 += crec1

            crec2 = (c2 * p2) / 100
            c2 += crec2
            #print(crec2)

            anios += 1
        print(anios, "anios")


while i <= CantidadTest:
    population_Incrase()
    i+=1
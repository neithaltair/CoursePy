a = float(input("a"))
b = float(input("b"))
c = float(input("c"))

if a >= (b+c):
    print("No forma triangulo")

elif a**2 == (b**2+c**2):
    print("Triangulo Rectuangulo")

elif a**2 > (b**2+c**2):
    print("Triangulo Obtusangulo")

elif a**2 < (b**2+c**2):
    print("Triangulo acutangulo")

elif (a==b and b==c):
    print("Triangulo Equilatero")

elif (a==b and a != c) or (c==a and a != b) or (b==c and c != a):
    print("Triangulo Isoceles")

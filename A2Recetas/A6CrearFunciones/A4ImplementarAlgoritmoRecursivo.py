#Receta 6-4: implementar un algoritmo recursivo

def calcularFactorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcularFactorial(n-1)

print(calcularFactorial(5))

# 5 = 5*4*3*2*1 = 120
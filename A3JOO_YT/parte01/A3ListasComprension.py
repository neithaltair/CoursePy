numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(type(numeros))
print(len(numeros))
print(numeros)

print()

paresTriplicados = []

for n in numeros:
    if n % 2 == 0:
        paresTriplicados.append(n * 3)

print(type(paresTriplicados))
print(len(paresTriplicados))
print(paresTriplicados)
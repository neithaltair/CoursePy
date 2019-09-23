names = ["neith","htien","riatla","altair"]

# For básico
for nomb in names:
    print("Print a array",nomb)

print("_____________________________________________________________________________")
# Print the chars in string 
string = "Content to add"
for char in string:
    print("print the characters in String",char)

print("_____________________________________________________________________________")
# Print numbers 
for number in range(11):
    print(number)

print("_____________________________________________________________________________")
# Print numbers 2 in 2
for number1 in range(2, 20, 2):
    print(number1)

print("_____________________________________________________________________________")
# Break the bucle in a specific number
for number2 in range(20):
    if (number2==14):
        break
    print(number2)

print("_____________________________________________________________________________")

# Jump a specific number and continue
for number3 in range(40):
    if(number3==20):
        continue
    print(number3)

print("_____________________________________________________________________________")

# for doble
for numero1 in range(1,6):
    for numero2 in range(5,11):
        print(numero1, numero2)

        
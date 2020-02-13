number = float(input())

if (number >= 0 and number <= 25):
    print("Interval [0,25]")

elif (number > 25 and number <= 50):
    print("Interval (25,50]")

elif (number > 50 and number <= 75.00):
    print("Interval (50,75]")

elif (number > 75 and number <= 100.00):
    print("Interval (75,100)")

else:
    print("Fora intervalo")
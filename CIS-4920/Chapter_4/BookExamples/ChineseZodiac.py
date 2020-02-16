
year = eval(input("Enter a year: "))
zodiacYear = year % 12

if zodiacYear == 0:
    print("Monkey")
elif zodiacYear == 1:
    print("Rooster")
elif zodiacYear == 2:
    print("Dog")
elif zodiacYear == 3:
    print("Pig")
elif zodiacYear == 4:
    print("Rat")
elif zodiacYear == 5:
    print("Ox")
elif zodiacYear == 6:
    print("Tiger")
elif zodiacYear == 7:
    print("Rabbit")
elif zodiacYear == 8:
    print("Dragon")
elif zodiacYear == 9:
    print("Snake")
elif zodiacYear == 10:
    print("Horse")
else:
    print("Sheep")
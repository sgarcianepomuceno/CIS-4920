import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

max = number1 if number1 > number2 else number2

print(max)
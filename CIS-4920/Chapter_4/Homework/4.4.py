'''This program generate two random integers and allows the user to enter the sum the integers.
If the user is correct, then it prints "True" and "False" if the user is incorrect.'''

import random

# Generate two integers between 0 and 100.
number1 = random.randint(0,100)
number2 = random.randint(0,100)

# User enters their answer.
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

# Compares the answer the user provided with the correct answer.
if answer == number1 + number2:
    print("True")
else:
    print("False")
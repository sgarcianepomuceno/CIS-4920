'''This program computes the average of three integers the user enters.
The difference between this code and the other code is one line is used
to enter three integers.'''

# Allows user to enter three integers.
number1, number2, number3 = eval(input(
    "Enter three integers separated by commas: "))

# Computes average of three integers the user entered.
average = (number1 + number2 + number3) / 3

# Display result
print("The average of",number1, number2, number3, "is", average)
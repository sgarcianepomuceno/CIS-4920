'''This code computes the average of three
integers entered by the user.'''

# This code allow users to enter three integers.
number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second number: "))
number3 = eval(input("Enter the third number: "))

# Computes average
average = (number1 + number2 + number3) / 3

# Display results
print("The average of", number1, number2,
      number3, "is", average)
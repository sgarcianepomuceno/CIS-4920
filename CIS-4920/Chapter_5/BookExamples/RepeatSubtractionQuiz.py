
import random

# Generate two random single-digit integers.
number1 = random.randint(0,9)
number2 = random.randint(0,9)

# if number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1

# Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + ' - ' + str(number2) + '? '))

# Repeatedly ask the question until the answer is correct
while answer != number1 - number2:
    answer = eval(input("Wrong answer. Try again. What is "
                        + str(number1) + ' - ' + str(number2) + '? '))
print("You got it!")
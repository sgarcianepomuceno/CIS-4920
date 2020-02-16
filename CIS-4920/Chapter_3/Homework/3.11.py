''' This program will display a 4 digit integer in reverse that the user entered.'''

# User enters a 4 digit integer.
number = eval(input("Enter an integer: "))
reverse = 0

# Loop to reverse integer user entered.
while(number > 0):
    a = number % 10
    reverse = (reverse * 10) + a
    number = number // 10

# Display reverse number.
print(reverse)
'''This program allows a user to enter three integers and arranges them in ascending order.'''

# User enters three integers
a, b, c = eval(input("Enter three integers: "))

# Display min, middle, max.
print(min(a,b,c), end = ' ')
print((a + b + c) - max(a,b,c) - min(a,b,c), end = ' ')
print(max(a,b,c))
'''THis program prints a table.'''

# Assign variables.
a = 1
b = 2

# Create table.
print('a\t b\t a ** b')
while a < 6:
    print(a, '\t', b, '\t', a ** b)
    a += 1
    b += 1
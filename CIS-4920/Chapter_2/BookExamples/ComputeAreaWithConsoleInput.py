'''This code allow users to enter a value for radius
and computes the area of a circle using the entered
value.'''

# This allows the user to input a value for radius.
radius = eval(input("Enter a value for radius: "))

# Compute area.
area = radius * radius * 3.14159

# Display results
print("The area for the circle of radius", radius,
      "is", area)
'''This program will display a circle and its area on turtle. '''

import turtle

# Declare variables.
PI = 3.14159

# User will enter the center and radius of the circle.
x, y = eval(input("Enter the center of the circle(x,y): "))
radius = eval(input("Enter the radius of the circle: "))

# Compute area.
area = PI * radius ** 2

turtle.dot()
#turtle.circle(50)


# Display circle using the 
turtle.penup()
turtle.goto(x // 2, y // 2)
turtle.pendown()
turtle.write("Area")
turtle.circle(radius)


turtle.done()
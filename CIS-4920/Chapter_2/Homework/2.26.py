'''This program will display a circle and its area on turtle. '''

import turtle

# Declare variables.
PI = 3.14159

# User will enter the center and radius of the circle.
x, y = eval(input("Enter the center of the circle(x,y): "))
radius = eval(input("Enter the radius of the circle: "))

# Compute area.
area = PI * radius ** 2

# Display circle using the 
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot()
turtle.write(format(area, ".2f"))

turtle.penup()
turtle.goto(x , y - radius)
turtle.pendown()
turtle.circle(radius)


turtle.done()
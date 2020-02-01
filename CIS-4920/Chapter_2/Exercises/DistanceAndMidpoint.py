'''This program will calculate the distance between two points
that the user enters and will display the points and the distance
on turtle.'''

# Turtle is imported to use graphics.
import turtle

# User enters two coordinates.
x1, y1 = eval(input("Enter two points for Point 1 (x1, y1): "))
x2, y2 = eval(input("Enter two points for Point 2 (x2, y2): "))

# Distance is computed.
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Arrow is moved to Point 1. 
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")

# Line is drawn to Point 2.
turtle.goto(x2, y2)
turtle.write("Point 2")
 
# Line is drawn between Point 1 and Point 2.
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()
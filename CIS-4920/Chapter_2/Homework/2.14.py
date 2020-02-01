'''This program will use three points entered by the user to
display a triangle and the area of the triangle on turtle.'''

import turtle

# User will enter three coordinates.
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle (x,y): "))

# Compute length of all three sides.
side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

# Compute area.
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

# Display result.
print(int(area * 100) / 100)

# Display triangle and the three points.
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("Point 1")

turtle.goto(x2,y2)
turtle.pendown()
turtle.write("Point 2")

turtle.goto(x3,y3)
turtle.pendown()
turtle.write("Point 3")
turtle.goto(x1,y1)

# Display area on turtle.
turtle.penup()
turtle.goto(-250,250)
turtle.write("Area:")
turtle.penup()
turtle.goto(-220,250)
turtle.write(int(area * 100) / 100)

turtle.done()
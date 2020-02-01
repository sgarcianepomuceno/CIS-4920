'''Area and perimeter of a rectangle with width and height of
4.5 and 7.9 respectively that displays the area and perimeter'''

import turtle

# Declare variables. THE SPECIFICATIONS WERE INCREASED BY 20
# BECAUSE THE RECTANGLE WAS TOO SMALL.
height = 7.9
width = 4.5

# Compute area and perimeter.
area = int(width * height * 100) / 100
perimeter = 2 * (width + height)

# Draw rectangle with specified dimensions.
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)

# Display area on graphic.
turtle.penup()
turtle.goto(0, 55)
turtle.write("Area: ")
turtle.penup()
turtle.goto(30,55)
turtle.write(area)

# Display  on graphic.
turtle.penup()
turtle.goto(0, 40)
turtle.write("Perimeter: ")
turtle.penup()
turtle.goto(50,40)
turtle.write(perimeter)

turtle.done()
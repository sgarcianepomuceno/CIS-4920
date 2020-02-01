'''Area and perimeter of a circle with a radius(5.5) that
displays the area and perimeter'''

import turtle

# Declare variables.
radius = 5.5
PI = 3.14159

# Compute area and perimeter.
area = radius * radius * PI
perimeter = 2 * radius * PI

# Display area.
turtle.circle(radius)
turtle.penup()
turtle.goto(radius + 25, 40)
turtle.pendown()
turtle.write("Area")
turtle.penup()
turtle.goto(radius + 55, 40)
turtle.pendown()
turtle.write(area)

# Display perimeter.
turtle.penup()
turtle.goto(radius + 25, 20)
turtle.pendown()
turtle.write("Perimeter")
turtle.penup()
turtle.goto(radius + 75, 20)
turtle.pendown()
turtle.write(perimeter)


turtle.done()
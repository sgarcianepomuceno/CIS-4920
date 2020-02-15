
import turtle

# Drawing a triangle.
turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3)

# Drawing a square.
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4)

# Drawing a pentagon.
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5)

# Drawing a hexagon.
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6)

# Drawing a circle.
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)

turtle.done()
'''This program displays a square with
a cross inside of the square in turtle.'''

import turtle

# Displaying square.
turtle.penup()
turtle.goto(-80,100)
turtle.pendown()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)


# Displaying cross inside square.
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.backward(200)

turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.right(90)
turtle.forward(200)

turtle.done()
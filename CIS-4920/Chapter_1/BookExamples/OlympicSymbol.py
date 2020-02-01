'''This program displays on the console  five rings that resemble
the Olympic Rings'''

import turtle

# Creates a blue ring with a radius of 45.
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

# Creates a black ring with a radius of 45.
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

# Creates a red ring with a radius of 45.
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

# Creates a yellow ring with a radius of 45.
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

# Creates a green ring with a radius of 45.
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.done()
'''This program creates the olympics rings using the radius the user enters.'''

import turtle

radius = eval(input("Enter the radius: "))

# Creates a blue ring with a radius of 45.
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(radius)

# Creates a black ring with a radius of 45.
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(radius)

# Creates a red ring with a radius of 45.
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(radius)

# Creates a yellow ring with a radius of 45.
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(radius)

# Creates a green ring with a radius of 45.
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()
turtle.done()
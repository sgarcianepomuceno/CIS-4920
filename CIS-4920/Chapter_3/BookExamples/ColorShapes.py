
import turtle

# Drawing a red triangle. 
turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 3)
turtle.end_fill()

# Drawing a blue square.
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40, steps = 4)
turtle.end_fill()

# Drawing a green pentagon.
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(40, steps = 5)
turtle.end_fill()

# Drawing a yellow hexagon.
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40, steps = 6)
turtle.end_fill()

# Drawing a purple circle.
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40)
turtle.end_fill()

# Write "Cool Colorful Shapes"
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool Colorful Shapes", font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
import turtle

x, y = eval(input("Enter the center of the circle: "))
radius = eval(input("Enter the radius of the circle: "))

turtle.dot()

turtle.penup()
turtle.goto(x,radius)
turtle.pendown()
turtle.write(radius * radius * 3.14)

turtle.penup()
turtle.goto(x,radius - radius)
turtle.pendown()
turtle.circle(radius)
turtle.hideturtle()

turtle.done()
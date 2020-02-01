import math
import time
import turtle

#a = chr(random.int(065,090))
# GMT seconds.
GMTSeconds = int(time.time())
remainingSeconds = GMTSeconds % 60

# GMT minutes.
GMTMinutes = GMTSeconds // 60
remainingMinutes = GMTMinutes % 60

# GMT hours.
GMTHours = GMTMinutes // 60
remainingHours = GMTHours % 24

# Eastern hour.
if remainingHours <= 5:
    EasternHour = remainingHours - 5 + 24 
elif remainingHours > 5:
    EasternHour = remainingHours - 5
    
print(remainingMinutes, "minutes")


height = eval(input("Enter length: "))
width = eval(input("Enter width: "))

turtle.penup()
turtle.left(90)
turtle.forward(height/2)
turtle.right(90)
turtle.pendown()
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.home()

turtle.done()
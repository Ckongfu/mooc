#PythonDraw

import turtle
turtle.setup(650,350,300,300)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor(0,0,0)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,40)
turtle.forward(40)
turtle.circle(18,180)
turtle.fd(30)
turtle.done()



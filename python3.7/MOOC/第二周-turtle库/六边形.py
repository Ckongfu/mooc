import turtle as tu

tu.setup(800,800)
tu.penup()
tu.pensize(7)
tu.pencolor(0,0,0)
tu.fd(-100)
tu.pendown()
k=60
for i in range(6):
    tu.seth(k)
    tu.fd(200)
    k+=-60
tu.hideturtle()
tu.done()

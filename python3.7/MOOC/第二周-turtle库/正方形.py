import turtle as tu

tu.setup(800,800)
tu.penup()
tu.pensize(10)
tu.pencolor(0,0,0)
tu.pendown()
k=90
for i in range(4):
    tu.seth(k)
    tu.fd(300)
    k+=-90

tu.done()


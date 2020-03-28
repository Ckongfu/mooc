import turtle as tu

tu.setup(800,800)
tu.pencolor(0.192,0.192,0.192)
tu.penup()
tu.forward(-100)
tu.pensize(10)
tu.pendown()
tu.circle(40)#在画笔左侧40像素的地方为圆点，画圆

tu.up()
tu.fd(20)
tu.left(90)
tu.fd(40)
tu.pendown()
tu.circle(-40)
for i in range(2):
    tu.penup()
    tu.right(90)
    tu.fd(60)
    tu.left(90)
    tu.pendown()
    tu.circle(-40) #在画笔右侧40像素的地方为圆点，画圆


tu.done()


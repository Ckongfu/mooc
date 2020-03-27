import turtle as tu
tu.speed(5)
tu.setup(800,800)
tu.penup()
tu.left(90)
tu.fd(100)
tu.right(90)
tu.pensize(7)
tu.pencolor('blue')
tu.pendown()

for i in range(9): #9条边 循环九次
    tu.fd(150)
    tu.left(80) #每个内角角度为80度

tu.hideturtle()
tu.done()

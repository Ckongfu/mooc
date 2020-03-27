import turtle as tu

k=45
for i in range(4):
    tu.seth(k)
    tu.fd(150)
    tu.left(90)
    tu.circle(150,45)
    tu.goto(0,0)
    k+=90

tu.done()

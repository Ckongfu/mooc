import turtle as tu
def drawGap():
    tu.penup()
    tu.fd(5)
def drawLine (draw):
    drawGap()
    tu.pendown() if draw else tu.penup()
    tu.fd(40)
    drawGap()
    tu.right(90)
def drawDight(dight):
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9,] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    tu.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    tu.left(180)
    tu.penup()
    tu.fd(20)
def drawDate(date):
    for i in date:
        drawDight(eval(i))
def main():
    tu.setup(800,350,200)
    tu.penup()
    tu.fd(-300)
    tu.pensize(5)
    drawDate('20190321')
    tu.hideturtle()
    tu.done()
main()

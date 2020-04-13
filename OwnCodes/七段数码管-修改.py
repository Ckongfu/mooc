import turtle as tu
import time
def drawGap():
    tu.penup()
    tu.fd(5)

def drawLine(draw):#通过传递参数draw来判断画笔的抬起或落下
    drawGap()
    if draw==True:
        tu.pendown()
    else:
        tu.penup()
    tu.fd(40)
    drawGap()
    tu.right(90)

def drawDigit(digit): #通过数字绘制七段数码管
    drawLine(1) if digit in [2,3,4,5,6,8,9] else drawLine(0)
    drawLine(1) if digit in [0,1,3,4,5,7,8,9] else drawLine(0)
    drawLine(1) if digit in [0,2,3,5,6,8,9] else drawLine(0)
    drawLine(1) if digit in [0,2,6,8] else drawLine('')
    tu.left(90)
    drawLine(1) if digit in [0,4,5,6,8,9] else drawLine('')
    drawLine(1) if digit in [0,2,3,5,6,7,8,9] else drawLine('')
    drawLine(1) if digit in [0,1,2,3,4,7,8,9] else drawLine('')
    tu.left(180)
    tu.penup()
    tu.fd(40)

def drawDate(date):
    tu.pencolor('red')
    for i in date:
        if i =='-':
            tu.write('年',font=('Arial',30,"normal"))
            tu.pencolor('green')
            tu.fd(40)
        elif i =='=':
            tu.write('月',font=('Arial',30,'normal'))
            tu.fd(40)
        elif i =='+':
            tu.write('日',font=("Arial",30,'normal'))
        else:
            drawDigit(eval(i))

def main():
    tu.setup(900,350,200,200)
    tu.penup()
    tu.fd(-400)
    tu.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    tu.hideturtle()
    tu.done()
main()


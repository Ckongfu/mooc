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
    drawLine(1) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(0)
    drawLine(1) if digit in [0,2,3,5,6,8,9] else drawLine(0)
    drawLine(1) if digit in [0,2,6,8] else drawLine('')
    tu.left(90)
    drawLine(1) if digit in [0,4,5,6,8,9] else drawLine('')
    drawLine(1) if digit in [0,2,3,5,6,7,8,9] else drawLine('')
    drawLine(1) if digit in [0,1,2,3,4,7,8,9] else drawLine('')
    tu.left(180)
    tu.penup()
    tu.fd(-40) #每次绘制完数字以后退回到原点

def Counttime(Time=eval(input('请输入倒计时（秒）：'))):
    for i in range (Time,-1,-1):
        if Time<10:
            tu.hideturtle()#隐藏画笔
            drawDigit(i)
            time.sleep(1) #等候1秒
            tu.clear() #清除当前数字

def main():
    tu.setup(500,500,200,200)
    tu.penup()
    tu.fd(-50)
    tu.pensize(5)
    Counttime()
    #drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    tu.hideturtle()
    tu.goto(0,0)
    tu.write('倒计时结束',font=('Arial',30,"normal"))
    time.sleep(3)#程序等待3秒退出
    #tu.done()

main()


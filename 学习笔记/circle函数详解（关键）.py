import turtle as t
'''

    circle(x,y)函数中，圆心数值的正负，决定海龟圆心在海龟的左右：正值圆心在海龟左侧，负值圆心在海龟右侧；
角度值的正负决定画弧的时候前进还是倒退：角度为正，是前进画弧线，角度为负值，后退画弧线

'''
t.speed(1)
t.seth(90)
t.fd (100)
t.bk(200)
t.penup()

t.goto(0,0)
t.seth(0)
t.pd()
t.fd(100)
t.bk(200)
t.penup()
t.goto(0,0)
t.pendown()         #建立一个二维坐标系 海龟恢复至起始坐标，角度复原为0度

k=1
for x in [90,-90]:       #测试正负圆心和角度所画出的弧线的情况
    for i in [100,-100]:

        t.pendown()
        t.circle(i,x)
        t.penup()
        t.goto(0,0)    #小海龟回到原点
        t.seth(0)      #小海龟的角度归零
        print('第',k,'次 circle',[i,x])
        k+=1
t.done()


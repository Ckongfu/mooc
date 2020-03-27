import turtle as tu
tu.setup(950,650)
tu.penup() #抬起画笔
tu.fd(-250)#画笔向后移动250个像素点
tu.pendown() #落下画笔
tu.pensize(25) #设定画笔的粗为 25个像素点
tu.pencolor('purple')#设定画笔的颜色为紫色
tu.seth(-40) #设定画笔起始时的角度为-40度

for i in range(5):   #让画笔循环4次画圆弧
    tu.circle(40,80)  #绘制在画笔左侧，半径为40像素、角度为80的圆弧
    tu.circle(-40,80)#绘制在画笔右侧，半径为40像素、角度为80的圆弧

tu.circle(40,80/2)
tu.fd(40)
tu.circle(16,180)
tu.fd(40*2/3)
tu.hideturtle() #隐藏画笔图标
tu.done() #画完之后不执行其他操作

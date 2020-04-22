#自动绘制轨迹 300，0，144，1，0，0
#第一位：行进距离
#第二位：转向判断0-左转，1-右转
#第三位：转向角度
#第四位-最后：RGB色彩体系（0-1之间的浮点数）
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
#数据读取
datals=[]
f=open("/Users/zouguannan/Downloads/b.txt")
for line in f:
    line=line.replace("\n","")
    datals.append(list(map(eval,line.split(','))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

t.done()
